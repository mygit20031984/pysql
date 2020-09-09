import pandas as pd

xl = pd.ExcelFile("C:/Users/Owner/PycharmProjects/pysql/code_scripts/Input_file.xlsx")
dfx1 = xl.parse("Sheet1")

p = dfx1['FixWidth'][0]
print(p)

widths = p

df = pd.read_fwf("C:/Users/Owner/PycharmProjects/pysql/Test_Files/file_fixwidth.txt", widths=widths)
print(df)
