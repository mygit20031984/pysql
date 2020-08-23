import pandas as pd
import pandasql
import datacompy
from datetime import datetime

df1 = pd.read_csv("file1.csv")
df2 = pd.read_csv("file2.csv")

compare = datacompy.Compare(
    df1,
    df2,
    on_index=True,
    #    join_columns=2,  #You can also specify a list of columns
    abs_tol=0,  # Optional, defaults to 0
    rel_tol=0,  # Optional, defaults to 0
    df1_name='Original',  # Optional, defaults to 'df1'
    df2_name='New'  # Optional, defaults to 'df2'
)
compare.matches(ignore_extra_columns=False)

filename1 = "File_Comp_Report" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"

with open(filename1, 'w') as wf:
    wf.write(compare.report())
