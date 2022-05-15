import pandas as pd

print("read_sql_table")
data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
data_df.sort_values(by='tag_id', inplace=True)
data_df.set_index('tag_id', inplace=True, drop=False)

