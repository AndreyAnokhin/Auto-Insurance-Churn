import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template

from preproc import process_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


def predict(model, xgb_m=None):
    try:
        df = pd.read_json(request.json)
    except:
        return jsonify({'error': 'invalid json request'})
    try:
        X = process_data(df, xgb_m)
    except:
        return jsonify({'error': 'process data error'})
    try:
        model = joblib.load(model)
    except:
        return jsonify({'error': 'invalid or no model'})

    try:
        predictions = model.predict(X)
        if xgb_m:
            predictions = np.asarray([np.argmax(line) for line in predictions])
        predictions = [int(p) for p in predictions]
    except:
        return jsonify({'error': 'prediction error'})

    return jsonify({'prediction': predictions})


@app.route('/predict_logreg', methods=['POST'])
def predict_logreg():
    return predict('logreg_model.pkl')


@app.route('/predict_xgboost', methods=['POST'])
def predict_xgboost():
    return predict('xgboost_model.pkl', xgb_m=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
