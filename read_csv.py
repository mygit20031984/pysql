import pandas as pd
import pandasql

df1 = pd.read_csv("file1.csv")

df2 = pandasql.sqldf('select * from df1 where Age > 30', globals())

print(df2)
# Read Pandas file#
