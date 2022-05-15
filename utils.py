from db import sql_select_next
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

def get_next_untagged():
    res = sql_select_next()
    return res


col_style = {'max-width': '10px', 'overflow': 'hidden', 'white-space': 'nowrap'}



def update_dataset():
    data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
    data_df.sort_values(by='tag_id', inplace=True)
    data_df.set_index('tag_id', inplace=True, drop=False)

    table_body = [html.Tr([
                    html.Td(row[4], style=col_style), # tag_id
                    html.Td(row[1], style=col_style), # comment
                    html.Td(row[6], style=col_style), # reverse
                    html.Td(row[2], style=col_style), # tag
                    html.Td(row[5], style=col_style), # copy_text
                    html.Td(row[7], style=col_style), # random1
                    html.Td(row[8], style=col_style), # random2
                    html.Td(
                        dbc.NavLink("Annotate", href=f"/annotate={row[4]}", active="exact", ),
                        style={'max-width': '20px'}
                    ),

                    ]) for row in tagged_df.values.tolist()]