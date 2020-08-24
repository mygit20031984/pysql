import pandas as pd
import compare
import SNT
import TNS
import find_dup
from datetime import datetime
import os

###
# 1. Source Records Not In Target
# 2. Target Records Not in Resource
# 3. Perfect Columns
# 4. Overall TestCase Status
# 5. Duplicate In Source
# 6. Duplicate In Target
###


# Setting Run ID & PArent Folder#
run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
parent_dir = "C:/Users/Owner/PycharmProjects/pysql/Results/Report_" + run_id
print(parent_dir)
os.makedirs(parent_dir)
print("RunID and Parent Dir is Set")

# Reading Input File#
xl = pd.ExcelFile("input_file.xlsx")
df = xl.parse("Sheet1")
x1 = df['Value'][1]
x2 = df['Value'][4]

# Creating 2 Dataframes#
df1 = pd.read_csv(x1)
df2 = pd.read_csv(x2)

# print("Find Duplicate records in DF1")
find_dup.find_dup1(df1, parent_dir, run_id)

# print("Compare Data Sets")
# Compare 2 data sets#
# compare.com1(df1, df2, run_id, parent_dir)


#
# print("Executing Data available in Source and not in Target")
# # Find Records available in Source and not in Target#
# SNT.SNT1(df1, df2, run_id, parent_dir)
#
# print("Executing Data available in Target and not in Source")
# # Find Records available in Target and not in Source#
# TNS.TNS1(df1, df2, run_id, parent_dir)
