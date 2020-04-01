import pandas as pd
import requests
import json


def check_api(server_url, api, data_json):
    url = server_url + api
    response = requests.post(url, json=data_json)

    try:
        print(response.json())
    except:
        print(response.text)


def main(server_url = 'http://127.0.0.1:5000/'):

    df = pd.read_csv('data/data.txt',  delimiter=';', encoding='utf8')
    df = df[df['DATA_TYPE'] == 'TRAIN']
    df = df.drop(labels = ["POLICY_IS_RENEWED", 'DATA_TYPE'],axis = 1)

    data = df.sample(1)
    data_json = data.to_json(orient='records', indent=2, force_ascii=False)

    print('Auto Insurance Churn API')
    print('Requests:')
    print(data_json)
    print('\nRequests answers:\n')
    print('--- LogisticRegression ---')
    print('Request from {}predict_logreg'.format(server_url))
    check_api(server_url, 'predict_logreg', data_json)
    print('\n--- XGboost ---')
    print('Request from {}predict_xgboost'.format(server_url))
    check_api(server_url, 'predict_xgboost', data_json)
    print()

import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        main(server_url=url)
    except:
        print('Incorrect url')
