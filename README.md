### Predictive Pulse: Symptom-Based Hypertension Triage System
# About the Project
Predictive Pulse is a Machine Learning web application designed to predict a patient's risk of hypertension (Normal, Stage-1, Stage-2, and Hypertensive Crisis) without relying on direct blood pressure readings.

Most baseline models use Systolic and Diastolic readings to predict hypertension, which causes Data Leakage (the model simply memorizes the medical definition rather than predicting anything). By strictly removing these physical measurements, Predictive Pulse acts as a true preventive triage tool, identifying hidden cardiovascular risks based purely on patient demographics, medical history, and physical symptoms.

# The Machine Learning Journey & Logic
This project was built focusing heavily on real-world medical AI constraints, specifically overcoming two major data science hurdles:

Eliminating Data Leakage: Systolic and Diastolic features were intentionally dropped. If a doctor already knows a patient's exact blood pressure, they do not need AI to diagnose them. The model is forced to learn the underlying symptoms leading up to a crisis.

Solving "Treatment Bias" (Confounding by Indication): During testing, the AI exhibited a contradiction: adding severe symptoms sometimes lowered the risk score to "Stage-1". Why? Because the AI learned that only critically ill patients are prescribed strict diets and blood pressure medications. To prevent the AI from using treatments to guess the disease, variables like TakeMedication and ControlledDiet were removed.

The Final Architecture: The resulting model relies on exactly 9 pure diagnostic features (e.g., Age, Symptom Severity, Visual Changes, Nosebleeds) evaluated by a robust Random Forest Ensemble. This ensures flawless logic: as physical symptoms get worse, the predicted clinical risk accurately scales to a Hypertensive Crisis.

# Key Features
Advanced Ensemble Modeling: Powered by a Random Forest algorithm that aggregates "votes" from hundreds of decision trees to find complex, non-linear symptom patterns.

Flawless Triage Logic: Free of confounding variables and data leakage, ensuring a safe, logical escalation of risk when severe symptoms are inputted.

Interactive Web Interface: A clean, professional clinical form built with Flask, allowing healthcare providers or users to do real-time patient assessments.

# Tech Stack
Programming Language: Python

Machine Learning: Scikit-Learn, Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Backend & Deployment: Flask, Pickle

Frontend: HTML5, CSS3

## Project Structure


Predictive-Pulse/
│
├── app.py                      # Flask application - handles all routes and prediction logic
├── requirements.txt            # List of Python packages needed to run the app
├── Procfile                    # For Heroku deployment (uses gunicorn)
├── vercel.json                # Vercel deployment configuration
├── runtime.txt                # Specifies Python 3.9 runtime
│
├── dataset/                    # Raw and processed data
│   ├── patient_data.csv       # The original, uncleaned dataset
│   ├── cleaned_dataset.csv     # Data after preprocessing and cleaning
│   ├── age_vs_stage.png       # Visualization: Age distribution by stage
│   ├── correlation_heatmap.png # Feature correlation analysis
│   ├── gender_distribution.png # Gender breakdown in dataset
│   ├── medication_vs_severity.png # Medication usage by severity
│   ├── pairplot.png          # Multi-feature comparison plot
│   └── stages_distribution.png # Target variable distribution
│
├── model/                      # Machine learning artifacts
│   ├── model.ipynb            # Jupyter notebook with full model training code
│   └── pro_model_pipeline.pkl # Serialized model (includes scaler + features)
│
├── notebooks/                 # Data analysis notebooks
│   ├── EDA.ipynb            # Exploratory Data Analysis - visualizations and insights
│   └── cleaning.ipynb        # Data cleaning process - handling missing values, encoding
│
├── static/                   # Static web assets
│   └── style.css            # Custom CSS with medical-themed design
│
└── templates/               # HTML templates
    └── index.html           # Main web form with Jinja2 templating
## Dataset Overview

### Features Used for Prediction

The model uses 11 features to make predictions:

| Feature Name | Description | Data Type | Values |
|--------------|-------------|-----------|--------|
| `Gender` | Patient's gender | Binary | 0 = Female, 1 = Male |
| `Age` | Patient's age in years | Numeric | 1-100+ |
| `History` | Family history of hypertension | Binary | 0 = No, 1 = Yes |
| `Patient` | Previously diagnosed with high BP | Binary | 0 = No, 1 = Yes |
| `TakeMedication` | Currently on BP medication | Binary | 0 = No, 1 = Yes |
| `Severity` | Overall symptom severity | Ordinal | 0 = None, 1 = Mild, 2 = Moderate, 3 = Severe |
| `BreathShortness` | Experiencing shortness of breath | Binary | 0 = No, 1 = Yes |
| `VisualChanges` | Experiencing visual disturbances | Binary | 0 = No, 1 = Yes |
| `NoseBleeding` | Frequent nosebleeds | Binary | 0 = No, 1 = Yes |
| `Whendiagnoused` | Years since first diagnosis | Numeric | 0-20+ |
| `ControlledDiet` | Following controlled diet | Binary | 0 = No, 1 = Yes |

### Target Variable: Stages

| Stage Value | Risk Level | Description |
|-------------|------------|-------------|
| 0 | Normal | No hypertension detected |
| 1 | Stage-1 | Mild hypertension |
| 2 | Stage-2 | Moderate to severe hypertension |
| 3 | Critical / Crisis | Hypertensive crisis - immediate attention required |

---

## Model Development Process

### Data Preprocessing

The raw dataset required several preprocessing steps:

1. **Handling Missing Values**: Identified and filled missing entries using appropriate strategies (mean for numeric, mode for categorical)
2. **Feature Scaling**: Applied StandardScaler to normalize all numeric features to the same scale
3. **Feature Selection**: Removed redundant features and selected the 11 most predictive features
4. **Train-Test Split**: Split data into training (80%) and testing (20%) sets

### Model Selection

Multiple algorithms were tested during development:

- **Logistic Regression**: Good baseline, linear decision boundaries
- **Decision Trees**: Interpretable, handles non-linear relationships
- **Random Forest**: Ensemble of trees, reduced overfitting
- **Support Vector Machine (SVM)**: Effective in high-dimensional spaces
- **K-Nearest Neighbors (KNN)**: Instance-based learning

The final model uses an ensemble approach (Random Forest / Gradient Boosting) which provided the best balance of accuracy and generalization.

### Validation Strategy

- **Stratified K-Fold Cross-Validation**: Ensured balanced class distribution across folds
- **GridSearchCV**: Hyperparameter tuning for optimal performance


## Deployment

### Vercel (Recommended)

The application is live on Vercel at:

**https://predictive-pulse.vercel.app/**

# Limitations & Future Improvements

### Current Limitations

1. **Binary Features**: Many features are binary (yes/no) when they could have more granularity
2. **Sample Size**: Model trained on limited dataset - more data would improve accuracy
3. **No Temporal Features**: Doesn't account for how symptoms change over time
4. **Simplified Severity**: Severity is self-reported on a 0-3 scale

### Potential Improvements

1. **Add more features**: Include BMI, exercise habits, sodium intake, stress levels
2. **Time-series modeling**: Track patient data over time
3. **Explainable AI**: Add SHAP or LIME for feature importance explanations
4. **User accounts**: Allow saving patient histories
5. **Export reports**: Generate PDF reports for patients

---

## Author

**Ayush Jha**


