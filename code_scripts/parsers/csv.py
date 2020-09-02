import pandas as pd


def csv1(f1, f2):
    # Creating 2 Dataframes#
    print("Creating Dataframes for Source and Target")
    p1 = pd.read_csv(f1)
    p2 = pd.read_csv(f2)
    return (p1, p2)
