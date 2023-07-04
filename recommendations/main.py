from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load('xgboost_model.pkl')

# Load encoders and scalers
le = joblib.load('label_encoder.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data, index=[0])

    # Preprocess data
    df['profession'] = le.transform(df['profession'])
    df[['annual_salary', 'months_ago_quoted']] = scaler.transform(df[['annual_salary', 'months_ago_quoted']])

    probabilities = model.predict_proba(df)
    return jsonify({'prediction': probabilities[0][1].item()})

if __name__ == '__main__':
    app.run(port=5001)
