import pandas as pd
import numpy as np
import json
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv('gym_data.csv')

# Target = Workout_Type
X = df.drop(columns=['Workout_Type'])
y = df['Workout_Type']

# Encode target
le = LabelEncoder()
y_enc = le.fit_transform(y)
workout_classes = le.classes_.tolist()  # e.g., ['Cardio','HIIT','Strength','Yoga']

# Feature engineering (must match what JS will do)
X['BMI_Class'] = pd.cut(X['BMI'], bins=[0,18.5,24.9,29.9,100], labels=[0,1,2,3])
X['HR_Burn_Ratio'] = X['Calories_Burned'] / (X['Max_BPM']+1)
X['Gender_Code'] = X['Gender'].map({'Male':0, 'Female':1})

# Select features (order matters for JS)
feature_cols = ['Age', 'Gender_Code', 'Weight (kg)', 'Height (m)', 'Max_BPM', 'Avg_BPM',
                'Resting_BPM', 'Session_Duration (hours)', 'Calories_Burned',
                'Fat_Percentage', 'Water_Intake (liters)', 'Workout_Frequency (days/week)',
                'BMI', 'BMI_Class', 'HR_Burn_Ratio']
X = X[feature_cols]

# Train Decision Tree (best from Phase 2)
dt = DecisionTreeClassifier(max_depth=10, random_state=42)
dt.fit(X, y_enc)

# Evaluate on test set (optional)
X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.2, random_state=42)
y_pred = dt.predict(X_test)
print(f"Decision Tree Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")

# Export tree to JSON
tree_ = dt.tree_
def export_tree(node):
    if tree_.feature[node] != -2:  # not leaf
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

# Save as JavaScript file
with open('tree_rules.js', 'w') as f:
    f.write("const decisionTree = " + json.dumps(tree_json, indent=2) + ";\n")
    f.write("const workoutTypes = " + json.dumps(workout_classes) + ";\n")

print("✅ tree_rules.js generated. Now run the interactive HTML.")