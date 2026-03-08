from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd 
import os

app = Flask(__name__)

# Load the Advanced Pro Model Pipeline
with open('model/pro_model_pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)
    model = pipeline['model']
    scaler = pipeline['scaler']
    feature_names = pipeline['features'] # We saved these earlier!

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Helper function to get form value with default
            def get_val(key, default=0):
                return int(request.form.get(key, default))
            
            # 11 Features 
            features = [
                get_val('Gender'),
                get_val('Age'),
                get_val('History'),
                get_val('Patient'),
                get_val('TakeMedication'),
                get_val('Severity'),
                get_val('BreathShortness'),
                get_val('VisualChanges'),
                get_val('NoseBleeding'),
                get_val('Whendiagnoused'),
                get_val('ControlledDiet')
            ]
            
            # FIX: Convert the input list into a Pandas DataFrame with the correct column names
            features_df = pd.DataFrame([features], columns=feature_names)
            
            # Scale features using the DataFrame
            scaled_features = scaler.transform(features_df)
            
            # Predict Risk Stage
            prediction = int(model.predict(scaled_features)[0]) # Cast to int for safety
            
            # Get Probability/Confidence scores
            probabilities = model.predict_proba(scaled_features)[0]
            confidence = round(max(probabilities) * 100, 2)
            
            stage_map = {0: 'Normal', 1: 'Stage-1', 2: 'Stage-2', 3: 'Critical / Crisis'}
            result = stage_map.get(prediction, "Unknown")
            
            return render_template('index.html', 
                                   prediction_text=f'Predicted Risk Level: {result}',
                                   confidence_text=f'AI Confidence Score: {confidence}%',
                                   form_data=request.form)
            
        except Exception as e:
            return render_template('index.html', prediction_text=f'Error in processing input: {e}', form_data=request.form)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)