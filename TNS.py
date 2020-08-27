def TNS1(df1, df2, run_id, parent_dir):
    df_tns = df2.merge(df1, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', 1)
    output_file_name = parent_dir + '/Target_not_in_Source' + run_id + '.csv'
    df_tns.to_csv(output_file_name, index=False)
    return len(df_tns.index)
