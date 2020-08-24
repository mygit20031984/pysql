import pandas as pd


def find_dup1(df, parent_dir, run_id):
    dfObj = pd.DataFrame(df)
    duplicateRows_fileName = parent_dir + '/Duplicates_' + run_id + '.csv'

    duplicateRowsDF = dfObj[dfObj.duplicated(keep=False)]
    duplicateRowsDF.to_csv(duplicateRows_fileName, index=False)
