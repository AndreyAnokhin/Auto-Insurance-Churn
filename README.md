# Auto-Insurance-Churn


# Docker
```
docker-compose up
```

# Testing the API
1. Run the Flask API locally for testing.
2. use HTTPie to make a GET request at the URL of the API. OR you can use the script `python api_check.py`

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

3. Example of successful output.
```json
{'prediction': [1]}
```

## Using script with heroku
```
python api_check.py https://auto-insurance-churn-api.herokuapp.com/
```
