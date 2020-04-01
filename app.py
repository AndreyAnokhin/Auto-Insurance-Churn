import joblib
import pandas as pd
from flask import Flask, jsonify, request

from preproc import process_data

app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>ML API</h2>"


@app.route("/train")
def train():
    pass


@app.route('/predict', methods=['POST'])
def predict():
    try:
        df = pd.read_json(request.json)
    except:
        return jsonify({'error': 'invalid json request'})
    try:
        X = process_data(df)
    except:
        return jsonify({'error': 'process data error'})
    try:
        model = joblib.load('model.pkl')
    except:
        return jsonify({'error': 'invalid or no model'})

    predictions = model.predict(X)
    predictions = [int(p) for p in predictions]
    return jsonify({'prediction': predictions})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
