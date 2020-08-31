import pandas as pd
import compare
import SNT
import TNS
import find_dup
from datetime import datetime
import os

# Test
#############################################
# Setting up Parent Folder and Run_ID
#############################################
run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
parent_dir = "C:/Users/Owner/PycharmProjects/pysql/Results/Report_" + run_id
print(parent_dir)
os.makedirs(parent_dir)
print("RunID and Parent Dir is Created")

# Reading Input File#
xl = pd.ExcelFile("input_file.xlsx")
df = xl.parse("Sheet1")
tc_cnt = df.count()

for i in df.index:
    x1 = df['Test_Case_Name'][i]
    x2 = df['Work_dir'][i]
    x3 = df['Report_Location'][i]
    x4 = df['Source File Path'][i]
    x5 = df['Source File Name'][i]
    x6 = df['Target File Path'][i]
    x7 = df['Target File Path'][i]
    x8 = df['Target File Name'][i]

    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x5)
    print(x6)
    print(x7)
    print(x8)

# Creating 2 Dataframes#
# df1 = pd.read_csv(x1)
# df2 = pd.read_csv(x2)
#
# #############################################
# # Find Duplicate from Data Sets
# #############################################
# # print("Find Duplicate records in Data Sets")
# df1_dup = find_dup.find_dup1(df1, 'Source', parent_dir, run_id)
# df2_dup = find_dup.find_dup1(df2, 'Target', parent_dir, run_id)
#
# print("Number of Duplicate Records in DF1  = " + str(df1_dup))
# print("Number of Duplicate Records in DF2  = " + str(df2_dup))
#
# #############################################
# # Remove Duplicate from Source and Target Data Sets
# #############################################
# print("Removing Duplicate records in Data Sets")
# df1 = df1.sort_values("ID", inplace=False)
# df1 = df1.drop_duplicates(subset="ID", keep='first', inplace=False)
#
# df2 = df2.sort_values("ID", inplace=False)
# df2 = df2.drop_duplicates(subset="ID", keep='first', inplace=False)
#
# # #####################################################
# # #Records available in Source Data Sets not in Target
# # #####################################################
# cnt_SNT = SNT.SNT1(df1, df2, run_id, parent_dir)
# print("Number of Records in Source and not in Target = " + str(cnt_SNT))
#
# # #####################################################
# # #Records available in Target Data Sets not in Source
# # #####################################################
# cnt_TNS = TNS.TNS1(df1, df2, run_id, parent_dir)
# print("Number of Records in Source and not in Target = " + str(cnt_TNS))
#
# # #####################################################
# # #Compare Source and Target Data Sets
# # #####################################################
# print("Compare Data Sets")
# compare.com1(df1, df2, run_id, parent_dir)
