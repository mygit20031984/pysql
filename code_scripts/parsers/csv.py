import pandas as pd


def csv1(df):
    # Creating 2 Dataframes#
    print("Creating Dataframes for Source and Target")
    df = pd.read_csv(df)
    return df
