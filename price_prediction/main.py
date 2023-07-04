from flask import Flask, render_template, request
import json
import jsonify
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
job_title_le = pickle.load(open("job_title_le.pkl", "rb"))
car_use_le = pickle.load(open("car_use_le.pkl", "rb"))
postcode_le = pickle.load(open("postcode_le.pkl", "rb"))

standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json(force=True)

        data = request.get_json(force=True)
        
        # The order of these features must match the order in which your model expects them
        input_features = [data['job_title'], data['car_use'], data['total_miles'], 
                          data['previous_claims'], data['postcode'], data['credit_score']]
        
        transformed_features = list(input_features)  # make a copy of the input list
        transformed_features[0] = job_title_le.transform([input_features[0]])[0]  # Transform 'job_title'
        transformed_features[1] = car_use_le.transform([input_features[1]])[0]  # Transform 'car_use'
        transformed_features[4] = postcode_le.transform([input_features[4]])[0]  # Transform 'postcode'

        # If 'previous_claims' was originally 'yes' or 'no', convert to 1 or 0
        if input_features[3].lower() == 'yes':
            transformed_features[3] = 1
        else:
            transformed_features[3] = 0

        prediction = model.predict([transformed_features])
        output = round(prediction[0], 2)
        
        return {'cheapest_quote': output}   

if __name__ == "__main__":
    app.run(debug=True, port=8001)

