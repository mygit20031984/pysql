def SNT1(df1, df2, run_id):
    df_snt = df1.merge(df2, how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', 1)
    output_file_name = 'source_not_in_Target' + run_id + '.csv'
    df_snt.to_csv(output_file_name, index=False)
