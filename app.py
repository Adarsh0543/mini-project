from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model and encoders
model = joblib.load('model.pkl')
encoders = joblib.load('encoders.pkl')  # Expecting a dict: {'Work class': le_object, ...}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # 1. Collect Numeric Features
            age = float(request.form['Age'])
            capital_gain = float(request.form['Capital-gain'])
            capital_loss = float(request.form['Capital-loss'])
            hours_per_week = float(request.form['Hours per week'])

            # 2. Collect & Encode Categorical Features (Using your loaded LabelEncoders)
            # We use .transform([value])[0] to get the integer
            work_class = encoders['Work class'].transform([request.form['Work class']])[0]
            education = encoders['Education'].transform([request.form['Education']])[0]
            marital_status = encoders['Marital status'].transform([request.form['Marital status']])[0]
            occupation = encoders['Occupation'].transform([request.form['Occupation']])[0]
            native_country = encoders['Native country'].transform([request.form['Native country']])[0]

            # 3. Handle One-Hot Encoding for Sex
            # Your features have 'Sex_ Female' and 'Sex_ Male'
            sex_input = request.form['Sex']
            
            if sex_input == 'Female':
                sex_female = 1
                sex_male = 0
            else:
                sex_female = 0
                sex_male = 1

            # 4. Create Final Feature Array
            # MUST match this order: ['Age', 'Work class', 'Education', 'Marital status', 'Occupation', 'Capital-gain', 'Capital-loss', 'Hours per week', 'Native country', 'Sex_ Female', 'Sex_ Male']
            features = np.array([[
                age, 
                work_class, 
                education, 
                marital_status, 
                occupation, 
                capital_gain, 
                capital_loss, 
                hours_per_week, 
                native_country, 
                sex_female, 
                sex_male
            ]])

            # 5. Predict
            prediction = model.predict(features)
            output = 'Income >50K' if prediction[0] == 1 else 'Income <=50K'

            return render_template('index.html', prediction_text=f'Prediction: {output}')

        except Exception as e:
            return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)