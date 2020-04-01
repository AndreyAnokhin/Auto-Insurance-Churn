import pandas as pd
import requests
import json


df = pd.read_csv('data/data.txt',  delimiter=';', encoding='utf8')
df = df.drop(labels = ["POLICY_IS_RENEWED", 'DATA_TYPE'],axis = 1)

data = df.sample(1)
data_json = data.to_json(orient='records', indent=2, force_ascii=False)

print('Send json request:')
print(data_json)


# for local test use url = 'http://127.0.0.1:5000/predict'
url = 'https://auto-insurance-churn-api.herokuapp.com/predict'


response = requests.post(url, json=data_json)
print('Get request:')
print(response.json())
