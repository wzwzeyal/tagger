from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=True)


def sql_select_next():
    with engine.begin() as connection:
        tbl_name = 'test_tsv'
        sql_str = f"SELECT * from {tbl_name} WHERE tag = 'Untagged' LIMIT 1"
        res = pd.read_sql_query(text(sql_str), con=connection)
        # res = connection.execute(text(sql_str))
    return res.iloc[0]


def get_tag_id(tag_id):
    with engine.begin() as connection:
        tbl_name = 'test_tsv'
        sql_str = f"SELECT * from {tbl_name} WHERE tag_id = {tag_id}"
        res = pd.read_sql_query(text(sql_str), con=connection)
        # res = connection.execute(text(sql_str))
    return res.iloc[0]


def sql_update(button_id, table_id):
    print(f'[sql_update]: Start')
    with engine.begin() as connection:
        tbl_name = 'test_tsv'
        col_name = 'tag'
        new_val = str(button_id)
        col_id_name = 'tag_id'

        sql_str = f"update {tbl_name} set {col_name}='{new_val}' WHERE {col_id_name}={table_id}"
        print(f'[sql_update]: sql_str: {sql_str}')
        print(f'[sql_update]: text(sql_str): {text(sql_str)}')
        res = connection.execute(text(sql_str))


def sql_count(where_clause=""):
    with engine.begin() as connection:
        tbl_name = 'test_tsv'
        # SELECT
        #    COUNT(*)
        # FROM
        #    table_name
        # WHERE
        #    condition;
        sql_str = f"SELECT COUNT(*) FROM {tbl_name} {where_clause}"

        print(f'[sql_update]: sql_str: {sql_str}')
        print(f'[sql_update]: text(sql_str): {text(sql_str)}')
        res = connection.execute(text(sql_str))
        keys = res.keys()
        print(f'[sql_count]: keys: {keys}')
        count = res.fetchone()['count']
        print(f'[sql_count]: count: {count}')
        print(f'[sql_update]: res: {res}')
    return count