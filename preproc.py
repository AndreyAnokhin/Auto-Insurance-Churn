import re
import pandas as pd
import xgboost as xgb


def process_data(df, xgb_m=None):
    df = df.drop(['POLICY_ID'], axis=1)

    cols_to_transform = [
    'POLICY_BRANCH',
    'VEHICLE_MAKE',
    'VEHICLE_MODEL',
    'INSURER_GENDER',
    'POLICY_CLM_N',
    'POLICY_CLM_GLT_N',
    'POLICY_PRV_CLM_N',
    'POLICY_PRV_CLM_GLT_N',
    'POLICY_YEARS_RENEWED_N',
    'CLIENT_REGISTRATION_REGION',
    'POLICY_INTERMEDIARY',
]
    # TODO: process categorical features and/or perform feature engineering
    # df = pd.get_dummies(df, columns = cols_to_transform)
    df = df.drop(cols_to_transform, axis=1)

    if xgb_m:
        regex = re.compile(r"\[|\]|<", re.IGNORECASE)
        df.columns = [regex.sub("_", col) if any(x in str(col) for x in set(('[', ']', '<'))) else col for col in df.columns.values]
        df = xgb.DMatrix(df)
    return df
