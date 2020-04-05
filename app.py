import json

import joblib
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, render_template, abort, make_response

from preproc import process_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


def predict(model, xgb_m=None):
    try:
        data_json = request.json
        if not isinstance(data_json, str):
            data_json = json.dumps(request.json)
        df = pd.read_json(data_json, orient='records')
    except:
        abort(make_response(jsonify(error='invalid json request'), 400))
    try:
        X = process_data(df, xgb_m)
    except:
        abort(make_response(jsonify(error='process data error'), 400))
    try:
        model = joblib.load(model)
    except:
        abort(make_response(jsonify(error='invalid or no model'), 400))

    try:
        predictions = model.predict(X)
        if xgb_m:
            predictions = np.asarray([np.argmax(line) for line in predictions])
        predictions = [int(p) for p in predictions]
    except:
        abort(make_response(jsonify(error='prediction error'), 400))

    return jsonify({'prediction': predictions})


@app.route('/predict_logreg', methods=['POST'])
def predict_logreg():
    return predict('logreg_model.pkl')


@app.route('/predict_xgboost', methods=['POST'])
def predict_xgboost():
    return predict('xgboost_model.pkl', xgb_m=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
