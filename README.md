# 🏋️ Gym Exercise Classification – Workout Type Predictor

## 📌 Problem Statement

**Title:** Personalized Workout Type Recommendation Using Machine Learning

**Problem:** Many people perform exercises that do not match their health condition or fitness level, leading to injury, burnout, or poor results. Generic workout plans ignore individual physiological parameters (age, BMI, heart rate, etc.).

**Objective:** To build a machine learning and deep learning system that predicts the most suitable workout type (Cardio, HIIT, Strength, Yoga) based on user health data. After prediction, the system also recommends specific exercises for that workout type.

**Outcome:** A Decision Tree model with 92.3% accuracy, integrated into an interactive web page hosted on GitHub Pages. Users enter their health metrics and receive a workout type + exercise suggestions.

---

## 📊 Dataset

- **Source:** Synthetic gym user session data.
- **Size:** 973 records, 15 original features.
- **Original Features:** Age, Gender, Weight (kg), Height (m), Max_BPM, Avg_BPM, Resting_BPM, Session_Duration (hours), Calories_Burned, Workout_Type, Fat_Percentage, Water_Intake (liters), Workout_Frequency (days/week), BMI.
- **Engineered Features:** `BMI_Class` (Underweight/Normal/Overweight/Obese), `HR_Burn_Ratio` (Calories_Burned / (Max_BPM+1)).
- **Target Variable:** `Workout_Type` (Cardio, HIIT, Strength, Yoga).

---

## 🤖 Models Used

### Machine Learning (Scikit-learn)
- Random Forest, Logistic Regression, Decision Tree, SVM, KNN
- Hyperparameter tuning via GridSearchCV (5-fold cross-validation)
- **Best Model:** Decision Tree (92.3% test accuracy)

### Deep Learning (TensorFlow/Keras)
- 3-layer Feedforward Neural Network: 128 → 64 → 32 neurons
- Activation: ReLU (hidden), Softmax (output)
- Optimiser: Adam (learning rate 0.001, adaptive reduction)
- Regularisation: Dropout (0.3), BatchNormalisation
- Callbacks: EarlyStopping (patience=10), ReduceLROnPlateau (factor=0.5, patience=5)

---

## 📈 Performance Comparison

| Model                  | Accuracy | Precision | Recall | F1 Score |
|------------------------|----------|-----------|--------|----------|
| Decision Tree          | 0.9231   | 0.9350    | 0.9231 | 0.9220   |
| Random Forest          | 0.8821   | 0.8823    | 0.8821 | 0.8819   |
| SVM                    | 0.8667   | 0.8670    | 0.8667 | 0.8667   |
| Logistic Regression    | 0.8513   | 0.8595    | 0.8513 | 0.8508   |
| Deep Learning (NN)     | 0.8462   | 0.8471    | 0.8462 | 0.8462   |
| KNN                    | 0.8410   | 0.8416    | 0.8410 | 0.8406   |

✅ **Decision Tree** is the best performing model – used in the interactive web predictor.

---

## 🚀 Live Interactive Predictor

You can try the model live (no installation required):

👉 **[Click here to predict your workout type](https://aswat0541.github.io/gym_workout_classifier/index.html)**

The predictor:
- Takes your health metrics (age, gender, weight, height, heart rates, etc.)
- Predicts the recommended workout type (Cardio, HIIT, Strength, Yoga)
- Shows specific exercises you can perform for that workout type


