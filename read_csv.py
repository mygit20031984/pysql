import pandas as pd
import compare
import SNT

run_id = '1'
xl = pd.ExcelFile("input_file.xlsx")
df = xl.parse("Sheet1")
x1 = df['Value'][1]
x2 = df['Value'][4]
print(x1)
print(x2)

df1 = pd.read_csv(x1)
df2 = pd.read_csv(x2)

compare.com1(df1, df2, run_id)
SNT.SNT1(df1, df2, run_id)
