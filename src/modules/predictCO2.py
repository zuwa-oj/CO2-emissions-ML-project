import requests
import json

data = {
    "Latitude": 40.7128,            # Change the value as needed for your point of interest
    "Population_density": 100       # Change the value as needed for your point of interest
}

url = "http://localhost:5000/predict"
response = requests.post(url, json=data)
if response.status_code == 200:
    predictions = json.loads(response.text)
    print(predictions)
else:
    print("Request failed with status code:", response.status_code)