import pandas as pd


def process_data(df):
    # df = df.drop(['POLICY_ID', 'DATA_TYPE', 'POLICY_IS_RENEWED'], axis=1)
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

    # df = pd.get_dummies(df, columns = cols_to_transform)
    df = df.drop(cols_to_transform, axis=1)

    return df
