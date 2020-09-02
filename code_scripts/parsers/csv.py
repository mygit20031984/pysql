import pandas as pd


def csv_df(df):
    df = pd.read_csv(df)
    return df
