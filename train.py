import pandas as pd
import numpy as np
import json
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv('gym_data.csv')

target = 'Workout_Type'
X = df.drop(columns=[target])
y = df[target]

# Encode target
le = LabelEncoder()
y_enc = le.fit_transform(y)
workout_classes = le.classes_.tolist()
print("Workout types:", workout_classes)

# Keep post‑session features, but remove Calories_Burned
post_session_cols = ['Max_BPM', 'Avg_BPM', 'Session_Duration (hours)', 'Water_Intake (liters)']
# Also keep pre‑session static features that are available after? Actually for post‑session we keep everything except target and Calories_Burned.
# But to be clear: we want all features except Calories_Burned.
# Let's define all features we will use (original minus Calories_Burned)
features_to_keep = ['Age', 'Gender', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM', 
                    'Resting_BPM', 'Session_Duration (hours)', 'Fat_Percentage', 
                    'Water_Intake (liters)', 'Workout_Frequency (days/week)', 'BMI']
X = X[features_to_keep]   # Calories_Burned is dropped

# Feature engineering (still needed for BMI_Class and HR_Burn_Ratio? We can keep or drop HR_Burn_Ratio since it uses Calories)
# But without Calories, HR_Burn_Ratio is not defined. So we remove HR_Burn_Ratio.
# We'll only add BMI_Class.
X['BMI_Class'] = pd.cut(X['BMI'], bins=[0,18.5,24.9,29.9,100], labels=[0,1,2,3])
X['Gender_Code'] = X['Gender'].map({'Male':0, 'Female':1})

# Final feature columns (order matters for JS)
feature_cols = ['Age', 'Gender_Code', 'Weight (kg)', 'Height (m)', 
                'Resting_BPM', 'Max_BPM', 'Avg_BPM', 'Session_Duration (hours)',
                'Fat_Percentage', 'Water_Intake (liters)', 'Workout_Frequency (days/week)',
                'BMI', 'BMI_Class']
X = X[feature_cols]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42, stratify=y_enc)

# Train Decision Tree
dt = DecisionTreeClassifier(max_depth=10, random_state=42, class_weight='balanced')
dt.fit(X_train, y_train)

# Evaluate
y_pred = dt.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Decision Tree (Post‑Session, no Calories) Test Accuracy: {acc:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=workout_classes))

# Export tree to JSON
tree_ = dt.tree_
def export_tree(node):
    if tree_.feature[node] != -2:
        return {
            "feature": feature_cols[tree_.feature[node]],
            "threshold": float(tree_.threshold[node]),
            "left": export_tree(tree_.children_left[node]),
            "right": export_tree(tree_.children_right[node])
        }
    else:
        class_id = np.argmax(tree_.value[node][0])
        return {"class": workout_classes[class_id]}

tree_json = export_tree(0)

with open('tree_rules.js', 'w') as f:
    f.write("const decisionTree = " + json.dumps(tree_json, indent=2) + ";\n")
    f.write("const workoutTypes = " + json.dumps(workout_classes) + ";\n")

print("✅ tree_rules.js generated (post‑session, no Calories).")
