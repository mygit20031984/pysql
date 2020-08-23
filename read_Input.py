import pandas as pd
from openpyxl import load_workbook

xl = pd.ExcelFile("input_file.xlsx")

df = xl.parse("Sheet1")

x = df['Input'][1]

print(x)
