import re

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from preproc import process_data

df = pd.read_csv('data/data.txt', delimiter=';')
df_train = df[df['DATA_TYPE'] == 'TRAIN']

df_train = process_data(df_train)
df_train = df_train.drop(['DATA_TYPE'], axis=1)

df_train["POLICY_IS_RENEWED"] = df_train["POLICY_IS_RENEWED"].astype(int)
y = df_train["POLICY_IS_RENEWED"].values
X = df_train.drop(labels=["POLICY_IS_RENEWED"], axis=1)

# Create Train & Test Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# Logistic Regression
print('Training Logistic Regression model')
logreg_model = LogisticRegression()
result = logreg_model.fit(X_train, y_train)

prediction_test = logreg_model.predict(X_test)
print("Accuracy = {}".format(accuracy_score(y_test, prediction_test)))

joblib.dump(logreg_model, 'logreg_model.pkl')

# XGboost

# Fix columns names
regex = re.compile(r"\[|\]|<", re.IGNORECASE)
X_train.columns = [regex.sub("_", col) if any(x in str(col) for x in set(('[', ']', '<'))) else col for col in
                   X_train.columns.values]
X_test.columns = [regex.sub("_", col) if any(x in str(col) for x in set(('[', ']', '<'))) else col for col in
                  X_test.columns.values]

D_train = xgb.DMatrix(X_train, label=y_train)
D_test = xgb.DMatrix(X_test, label=y_test)

param = {
    'eta': 0.3,
    'max_depth': 3,
    'objective': 'multi:softprob',
    'num_class': 3}

steps = 20
print('Training XGBoost model')
model = xgb.train(param, D_train, steps)
preds = model.predict(D_test)
best_preds = np.asarray([np.argmax(line) for line in preds])
print("Accuracy = {}".format(accuracy_score(y_test, best_preds)))

joblib.dump(model, 'xgboost_model.pkl')
