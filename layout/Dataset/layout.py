import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc, dash_table

col_style = {'max-width': '10px', 'overflow': 'hidden', 'white-space': 'nowrap'}

def update_datset_table():
    print(f'[update_datset_table]: Start')
    data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
    data_df.sort_values(by='tag_id', inplace=True)
    data_df.set_index('tag_id', inplace=True, drop=False)

    print(f'[update_datset_table]: : read data_df')

    table_header = [
        html.Tr([html.Th("ID"),  # 4
                 html.Th("Left", ),  # 1
                 html.Th("Right"),  # 6
                 html.Th("Tag"),  # 6
                 html.Th("Text1"),  # 7
                 html.Th("Text2"),  # 8
                 html.Th("Text3"),  # 9
                 ])
    ]

    print(f'[update_datset_table]: : header')

    values = data_df.values.tolist()

    # since we are adding the NavLink column we refrain using from_dataframe
    table_body = [html.Tr([
        html.Td(row[4], style=col_style),  # tag_id
        html.Td(row[1], style=col_style),  # comment
        html.Td(row[2], style=col_style),  # tag
        html.Td(row[6], style=col_style),  # reverse
        html.Td(row[5], style=col_style),  # copy_text
        html.Td(row[7], style=col_style),  # random1
        html.Td(row[8], style=col_style),  # random2
        html.Td(
            dbc.NavLink("Annotate", href=f"/annotate={row[4]}", active="exact", ),
            style={'max-width': '20px'}
        ),

    ]) for row in values]

    print(f'[update_datset_table]: : body')

    print(f'[update_datset_table]: End')

    return dbc.Table(
        table_header + table_body,  # striped=True,
        bordered=True,
        style={
            'max-height': 'calc(92vh)',
            'overflow-x': 'auto'
        }),

dataset_layout_style = {
    'max-height': 'calc(92vh)',
    'padding': '1rem',
}

dataset_layout = html.Div(
    id="dataset_layout",
    style={'display': 'none'}
)
