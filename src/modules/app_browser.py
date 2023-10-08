from flask import Flask, request, jsonify
import xgboost as xgb
import pickle
import pandas as pd

model_filename = "../../output/xgboost_regression_model.pkl"
with open(model_filename, 'rb') as model_file:
    xgb_model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    latitude = float(request.args.get('Latitude'))
    population_density = float(request.args.get('Population_density'))
    
    # Create a DataFrame with the received data
    data = {'Latitude': [latitude], 'Population_density': [population_density]}
    df = pd.DataFrame(data)
    
    # Make predictions using the loaded model
    predictions = xgb_model.predict(df)
    
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)


# Example usage:
# http://localhost:5000/predict?Latitude=40.7128&Population_density=1000

