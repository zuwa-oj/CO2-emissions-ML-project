from flask import Flask, request, jsonify
import xgboost as xgb
import pickle
import pandas as pd

model_filename = "../../output/xgboost_regression_model.pkl"
with open(model_filename, 'rb') as model_file:
    xgb_model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get the JSON data from the request
        df = pd.DataFrame(data, index=[0])  # Convert JSON data to a DataFrame
        predictions = xgb_model.predict(df)  # Make predictions using the loaded model
        return jsonify(predictions.tolist())  # Return predictions as JSON
    except Exception as e:
        return jsonify(error=str(e)), 500  # Return an error message with a 500 status code


if __name__ == '__main__':
    app.run(debug=True)