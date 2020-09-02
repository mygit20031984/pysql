import pandas as pd
from code_scripts import compare, ST, find_dup
from code_scripts.parsers import csv
from datetime import datetime
import os


#############################################
# Reading Input File
#############################################
xl = pd.ExcelFile("Input_file.xlsx")
dfx1 = xl.parse("Sheet1")
dfx2 = xl.parse("Sheet2")

#############################################
# Setting up Parent Folder and Run_ID
#############################################
run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
parent_dir = dfx2['Report_Location'][0] + "_" + run_id
print(parent_dir)
os.makedirs(parent_dir)
print("RunID and Parent Dir is Created")

for i in dfx1.index:
    TCN = dfx1['Test_Case_Name'][i]
    SFP = dfx1['Source File Path'][i]
    SFN = dfx1['Source File Name'][i]
    SFT = dfx1['Source_Type'][i]
    TFP = dfx1['Target File Path'][i]
    TFN = dfx1['Target File Name'][i]
    UK = dfx1['Unique_Keys'][i]
    RF = dfx1['Run_Flag'][i]
    TFT = dfx1['Target_Type'][i]

    f1 = SFP + SFN
    f2 = TFP + TFN
    print("====================================================")
    print("Please find below logs for Test Case Name = " + TCN)
    print("====================================================")

    ############################################
    # Create Dataframes using Parsers
    ############################################
    print("Creating Dataframes for Source and Target")
    if SFT == 'csv':
        df1 = csv.csv1(f1)

    if TFT == 'csv':
        df2 = csv.csv1(f2)

    if not os.path.exists(parent_dir + "/" + TCN):
        os.makedirs(parent_dir + "/" + TCN)

    ############################################
    # Find Duplicate from Data Sets
    ############################################
    print("Find Duplicate records in Data Sets")
    df1_dup = find_dup.find_dup1(df1, 'Source', parent_dir, run_id, TCN)
    df2_dup = find_dup.find_dup1(df2, 'Target', parent_dir, run_id, TCN)

    print("Number of Duplicate Records in DF1 for  " + TCN + " = " + str(df1_dup))
    print("Number of Duplicate Records in DF2 for  " + TCN + " = " + str(df2_dup))

    # #############################################
    # # Remove Duplicate from Source and Target Data Sets
    # #############################################
    print("Removing Duplicate records in Data Sets")
    df1 = df1.sort_values("ID", inplace=False)
    df1 = df1.drop_duplicates(subset="ID", keep='first', inplace=False)

    df2 = df2.sort_values("ID", inplace=False)
    df2 = df2.drop_duplicates(subset="ID", keep='first', inplace=False)

    # # #####################################################
    # # #Records available in Source Data Sets not in Target
    # # #####################################################
    diff = "Source_not_in_Target"
    cnt_ST = ST.ST1(df1, df2, run_id, parent_dir, TCN, diff)
    print("Number of Records in Source and not in Target = " + str(cnt_ST))

    # # #####################################################
    # # #Records available in Target Data Sets not in Source
    # # #####################################################
    diff = "Target_not_in_Source"
    cnt_ST = ST.ST1(df2, df1, run_id, parent_dir, TCN, diff)
    print("Number of Records in Source and not in Target = " + str(cnt_ST))

    # # #####################################################
    # # #Compare Source and Target Data Sets
    # # #####################################################
    print("Compare Data Sets")
    compare.com1(df1, df2, run_id, parent_dir, TCN)
