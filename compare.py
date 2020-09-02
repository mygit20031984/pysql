import datacompy

def com1(df1, df2, run_id, parent_dir, TCN):
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

    filename1 = parent_dir + "/" + TCN + "/Summary_Report" + run_id + ".txt"
    all_mismatches = parent_dir + "/All_Mismatches_Report_" + run_id + ".txt"

    with open(filename1, 'w') as wf:
        wf.write(compare.report())
