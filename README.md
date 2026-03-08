### Predictive-Pulse
# About the Project
Predictive Pulse is an end-to-end Machine Learning web application designed to predict a patient's risk of developing varying stages of hypertension (Normal, Stage-1, Stage-2, and Hypertensive Crisis).

Unlike basic models that rely on direct blood pressure readings (which causes data leakage and renders the predictive aspect useless), this advanced system acts as a true preventive triage tool. It predicts hypertension risk based purely on clinical symptoms, lifestyle factors, and medical history. This allows healthcare providers to identify hidden risks even when a blood pressure cuff is unavailable.

# Key Features
Symptom-Based Triage: Evaluates risk using 11 key demographic and clinical features (e.g., symptom severity, age, medication status, visual changes).

Data Leakage Mitigation: Intentionally removed deterministic variables (Systolic and Diastolic readings) to force the model to learn true underlying risk patterns rather than just memorizing medical thresholds.

Probability Breakdown: The frontend doesn't just give a single answer; it provides a transparent AI confidence score across all 4 stages, mimicking a real doctor's diagnostic thought process.

Interactive Web Interface: A clean, user-friendly clinical form built with Flask, allowing for real-time patient assessment.

# Tech Stack
Programming Language: Python

Machine Learning: Scikit-Learn, Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Backend & Deployment: Flask, Pickle

Frontend: HTML5, CSS3

# Machine Learning Pipeline Highlights
Exploratory Data Analysis (EDA): Visualized feature correlations, gender distributions, and symptom-to-stage mapping.

Data Preprocessing: Handled categorical encoding, standardized feature scaling using StandardScaler, and cleaned inconsistent data entries.

Model Evaluation: Tested multiple algorithms (Logistic Regression, Decision Trees, SVM, KNN).

Advanced Ensembling: Deployed an optimized ensemble model (Gradient Boosting / Random Forest) using GridSearchCV and Stratified K-Fold Cross-Validation to handle complex, overlapping medical symptoms effectively.

# Project Structure
Plaintext

predictive-pulse/
│
├── static/
│   └── style.css               # Frontend styling
│
├── templates/
│   └── index.html              # Web application interface
│
├── app.py                      # Flask backend and API routing
├── pro_model_pipeline.pkl      # Saved ML model & scaler 
├── cleaned_dataset.csv         # Processed data used for training
├── patient_data.csv            # Original raw dataset
└── README.md                   # Project documentation
