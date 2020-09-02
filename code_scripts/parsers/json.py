import pandas as pd


def json_df():
    df = pd.read_json(r'Path where you saved the JSON file\File Name.json')
    return df
