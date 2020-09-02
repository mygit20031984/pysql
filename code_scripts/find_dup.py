import pandas as pd
import os


def find_dup1(df, df_name, parent_dir, run_id, TCN):
    dfObj = pd.DataFrame(df)
    duplicateRows_fileName = parent_dir + "/" + TCN + '/Duplicates_in_' + df_name + "_" + run_id + '.csv'

    duplicateRowsDF = dfObj[dfObj.duplicated(keep=False)]
    duplicateRowsDF.to_csv(duplicateRows_fileName, index=False)
    cnt = len(duplicateRowsDF.index)
    return cnt
