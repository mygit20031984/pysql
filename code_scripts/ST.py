def ST1(dfx, dfy, run_id, parent_dir, TCN, SNT):
    df_st = dfx.merge(dfy, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', 1)
    output_file_name = parent_dir + "/" + TCN + "/" + SNT + "_" + run_id + ".csv"
    df_st.to_csv(output_file_name, index=False)
    return len(df_st.index)
