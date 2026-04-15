import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# ==========================================
# 1. LOAD DATA (robust path handling)
# ==========================================
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'gym_data.csv')
print(f"Loading CSV from: {csv_path}")
df = pd.read_csv(csv_path)

print("Dataset shape:", df.shape)
print("\nFirst 3 rows:\n", df.head(3))

# ==========================================
# 2. TARGET = Experience_Level
# ==========================================
target = 'Experience_Level'
X = df.drop(columns=[target])
y = df[target]

le = LabelEncoder()
y = le.fit_transform(y)
print("\nTarget classes:", le.classes_)
print("Class distribution (%):")
print(pd.Series(y).value_counts(normalize=True) * 100)

# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================
if 'BMI' in X.columns:
    X['BMI_Class'] = pd.cut(X['BMI'], bins=[0, 18.5, 24.9, 29.9, 100],
                            labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

if 'Calories_Burned' in X.columns and 'Max_BPM' in X.columns:
    X['HR_Burn_Ratio'] = X['Calories_Burned'] / (X['Max_BPM'] + 1)

# ==========================================
# 4. TRAIN/VAL/TEST SPLIT (64/16/20)
# ==========================================
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.2, random_state=42, stratify=y_temp)

print(f"\nData Split:")
print(f"Training   : {len(X_train)} ({len(X_train)/len(X)*100:.1f}%)")
print(f"Validation : {len(X_val)} ({len(X_val)/len(X)*100:.1f}%)")
print(f"Test       : {len(X_test)} ({len(X_test)/len(X)*100:.1f}%)")

# ==========================================
# 5. PREPROCESSING
# ==========================================
numeric_cols = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = X_train.select_dtypes(include=['object', 'str']).columns.tolist()

numeric_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# ==========================================
# 6. MACHINE LEARNING MODELS
# ==========================================
models = {
    'Random Forest': RandomForestClassifier(random_state=42, class_weight='balanced'),
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced'),
    'Decision Tree': DecisionTreeClassifier(random_state=42, class_weight='balanced'),
    'SVM': SVC(random_state=42, class_weight='balanced'),
    'KNN': KNeighborsClassifier()
}

param_grids = {
    'Random Forest': {'classifier__n_estimators': [100, 200], 'classifier__max_depth': [10, 20, None]},
    'Logistic Regression': {'classifier__C': [0.1, 1, 10]},
    'Decision Tree': {'classifier__max_depth': [5, 10, 20, None]},
    'SVM': {'classifier__C': [0.1, 1, 10], 'classifier__kernel': ['rbf', 'linear']},
    'KNN': {'classifier__n_neighbors': [3, 5, 7, 9]}
}

best_models = {}
val_results = []

for name, model in models.items():
    print(f"\n--- Training {name} ---")
    pipeline = Pipeline([('preprocessor', preprocessor), ('classifier', model)])
    grid = GridSearchCV(pipeline, param_grids[name], cv=5, scoring='accuracy', n_jobs=-1)
    grid.fit(X_train, y_train)
    best_models[name] = grid.best_estimator_
    y_val_pred = grid.predict(X_val)
    val_acc = accuracy_score(y_val, y_val_pred)
    val_results.append({'Model': name, 'Validation Accuracy': val_acc})
    print(f"  Validation Accuracy: {val_acc:.4f}")

# ==========================================
# 7. DEEP LEARNING MODEL
# ==========================================
print("\n--- Training Deep Learning Model (Neural Network) ---")

preprocessor.fit(X_train)
X_train_prep = preprocessor.transform(X_train)
X_val_prep = preprocessor.transform(X_val)
X_test_prep = preprocessor.transform(X_test)

input_dim = X_train_prep.shape[1]
num_classes = len(np.unique(y_train))

def build_model(input_dim, num_classes, dropout_rate=0.3, lr=0.001):
    model = Sequential([
        Dense(128, activation='relu', input_shape=(input_dim,)),
        BatchNormalization(),
        Dropout(dropout_rate),
        Dense(64, activation='relu'),
        BatchNormalization(),
        Dropout(dropout_rate),
        Dense(32, activation='relu'),
        BatchNormalization(),
        Dropout(dropout_rate),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer=Adam(learning_rate=lr),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

dl_model = build_model(input_dim, num_classes)

early_stop = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=5, min_lr=1e-6)

history = dl_model.fit(
    X_train_prep, y_train,
    validation_data=(X_val_prep, y_val),
    epochs=100,
    batch_size=32,
    callbacks=[early_stop, reduce_lr],
    verbose=1
)

y_pred_dl = np.argmax(dl_model.predict(X_test_prep), axis=1)
dl_metrics = {
    'Model': 'Deep Learning (Neural Network)',
    'Accuracy': accuracy_score(y_test, y_pred_dl),
    'Precision': precision_score(y_test, y_pred_dl, average='weighted'),
    'Recall': recall_score(y_test, y_pred_dl, average='weighted'),
    'F1 Score': f1_score(y_test, y_pred_dl, average='weighted')
}

# ==========================================
# 8. TEST SET EVALUATION
# ==========================================
test_results = []
for name, model in best_models.items():
    y_pred = model.predict(X_test)
    test_results.append({
        'Model': name,
        'Accuracy': accuracy_score(y_test, y_pred),
        'Precision': precision_score(y_test, y_pred, average='weighted'),
        'Recall': recall_score(y_test, y_pred, average='weighted'),
        'F1 Score': f1_score(y_test, y_pred, average='weighted')
    })

test_results.append(dl_metrics)
results_df = pd.DataFrame(test_results).sort_values('Accuracy', ascending=False)

print("\n" + "="*60)
print("TEST SET PERFORMANCE (including Deep Learning)")
print("="*60)
print(results_df.to_string(index=False))

# ==========================================
# 9. VISUALISATIONS
# ==========================================
metrics = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()
for i, metric in enumerate(metrics):
    ax = axes[i]
    sorted_df = results_df.sort_values(metric, ascending=False)
    sns.barplot(x='Model', y=metric, data=sorted_df, hue='Model', palette='viridis', legend=False, ax=ax)
    ax.set_title(f'Model Comparison - {metric}')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_ylim(0, 1)
plt.tight_layout()
plt.savefig('performance_with_dl.png')
plt.show()

# Confusion Matrix (best overall model)
best_name = results_df.iloc[0]['Model']
if best_name == 'Deep Learning (Neural Network)':
    y_pred_best = y_pred_dl
else:
    y_pred_best = best_models[best_name].predict(X_test)

cm = confusion_matrix(y_test, y_pred_best)
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title(f'Confusion Matrix - {best_name}')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('confusion_matrix.png')
plt.show()

# Feature Importance (Random Forest only)
if 'Random Forest' in best_models:
    rf_pipeline = best_models['Random Forest']
    preproc = rf_pipeline.named_steps['preprocessor']
    cat_features = preproc.named_transformers_['cat'].named_steps['onehot'].get_feature_names_out(categorical_cols)
    all_features = numeric_cols + list(cat_features)
    importances = rf_pipeline.named_steps['classifier'].feature_importances_
    indices = np.argsort(importances)[::-1][:10]
    plt.figure(figsize=(10,6))
    plt.title('Top 10 Feature Importances - Random Forest')
    plt.barh(range(10), importances[indices], color='teal')
    plt.yticks(range(10), [all_features[i] for i in indices])
    plt.xlabel('Importance')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    plt.show()

# ==========================================
# 10. INSIGHTS (FIXED classification_report)
# ==========================================
print("\n" + "="*60)
print("INSIGHTS")
print("="*60)
print(f"Best model: {best_name} with Accuracy = {results_df.iloc[0]['Accuracy']:.4f}")

# FIX: convert target names to strings
print("\nClassification Report (Best Model):")
print(classification_report(y_test, y_pred_best, target_names=[str(c) for c in le.classes_]))

print("\nValidation vs Test Accuracy (ML models):")
for name in best_models.keys():
    val_acc = next(item['Validation Accuracy'] for item in val_results if item['Model']==name)
    test_acc = results_df[results_df['Model']==name]['Accuracy'].values[0]
    diff = test_acc - val_acc
    print(f"  {name}: Val = {val_acc:.4f}, Test = {test_acc:.4f}, Diff = {diff:+.4f}")

print(f"\nDeep Learning - Best validation accuracy: {max(history.history['val_accuracy']):.4f}")