from requests import post

url = 'http://127.0.0.1:5000/predict'

dict_json = {
    'Pregnancies': 0,
    'Glucose': 100,
    'BloodPressure': 80,
    'Insulin': 56,
    'BMI': 40,
    'Age': 58,
}

r = post(url, json=dict_json)

print(r.status_code)
print(r.json)