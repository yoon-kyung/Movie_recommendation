def refining_df(raw_df):

    title_number_df = raw_df.groupby('title').count().sort_values('user')
    title_under_10 = title_number_df[title_number_df.user <= 10]
    title_under_10_list = list(title_under_10.index)

    for title in title_under_10_list:
        raw_df = raw_df[raw_df['title'] != title]

    new_data = raw_df.reset_index(drop=True)

    return new_df
