# Auto Insurance Churn API

The task: To predict is insurance policy renewed or not based on client data.
There is API for two models based on Logistic Regression and XGboost.

API urls:
```
http://<server_name>/predict_logreg
http://<server_name>/predict_xgboost
```

## How to install

For requirements see [Pipfile](Pipfile).

Create a virtual environment and install dependencies with [pipenv](https://github.com/pypa/pipenv):
```sh
pipenv install
pipenv shell
```
#### Run the server:
```sh
gunicorn --bind 127.0.0.1:5000 app:app
```

## Install and run with Docker
```
docker-compose up
```

## The server has run on Heroku 
Check it out - 
[https://auto-insurance-churn-api.herokuapp.com/](https://auto-insurance-churn-api.herokuapp.com/)

# Testing the API

- Run the Flask API locally for testing.
- use your HTTP client to make a POST request at the URL of the API with a json query.
API urls:
```
http://127.0.0.1:5000/predict_logreg
http://127.0.0.1:5000/predict_xgboost
```

A json example:
```json
[
  {
    "POLICY_ID":96457,
    "POLICY_BEGIN_MONTH":8,
    "POLICY_END_MONTH":8,
    "POLICY_SALES_CHANNEL":52,
    "POLICY_SALES_CHANNEL_GROUP":6,
    "POLICY_BRANCH":"Санкт-Петербург",
    "POLICY_MIN_AGE":41,
    "POLICY_MIN_DRIVING_EXPERIENCE":0,
    "VEHICLE_MAKE":"Ford",
    "VEHICLE_MODEL":"Kuga",
    "VEHICLE_ENGINE_POWER":150.0,
    "VEHICLE_IN_CREDIT":0,
    "VEHICLE_SUM_INSURED":950000.0,
    "POLICY_INTERMEDIARY":"509",
    "INSURER_GENDER":"M",
    "POLICY_CLM_N":"2",
    "POLICY_CLM_GLT_N":"1L",
    "POLICY_PRV_CLM_N":"N",
    "POLICY_PRV_CLM_GLT_N":"N",
    "CLIENT_HAS_DAGO":0,
    "CLIENT_HAS_OSAGO":0,
    "POLICY_COURT_SIGN":0,
    "CLAIM_AVG_ACC_ST_PRD":0.0,
    "POLICY_HAS_COMPLAINTS":0,
    "POLICY_YEARS_RENEWED_N":"0",
    "POLICY_DEDUCT_VALUE":10000.0,
    "CLIENT_REGISTRATION_REGION":"Санкт-Петербург",
    "POLICY_PRICE_CHANGE":0.43
  }
]
```

- Example of successful output:
```json
{"prediction": [1]}
```

## Check API with the script:
The script send random data from data/data.txt to both API urls:
```
python api_check.py 
```

## Using script with heroku
```
python api_check.py https://auto-insurance-churn-api.herokuapp.com/
```
## To retrain the models
```
python train_models.py
```
