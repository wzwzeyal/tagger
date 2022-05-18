import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc, dash_table


# col_style = {'max-width': '10px', 'overflow': 'hidden', 'white-space': 'nowrap'}
from layout.annotate.buttons.layout import buttons_dict


def update_dataset_table():
    print(f'[update_dataset_table]: Start')
    data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
    data_df.sort_values(by='tag_id', inplace=True)
    data_df.set_index('tag_id', inplace=True, drop=False)

    print(f'[update_dataset_table]: : read data_df')

    table_header = [
        html.Thead(
            html.Tr(
                [
                    html.Th("ID"),  # 4
                    html.Th("Left", ),  # 1
                    html.Th("Right"),  # 6
                    html.Th("Tag"),  # 6
                    html.Th("Text1"),  # 7
                    html.Th("Text2"),  # 8
                    html.Th("Text3"),  # 9
                    html.Th(""),
                ]
            ),
            id='table-head',
        ),
    ]

    print(f'[update_dataset_table]: : header')

    values = data_df.values.tolist()

    # since we are adding the NavLink column we refrain using from_dataframe
    table_body = [
        html.Tbody(
            [
                html.Tr([
                    html.Td(row[4], ),  # tag_id
                    html.Td(row[1], ),  # comment
                    html.Td(row[6], ),  # reverse
                    html.Td(row[2], ),  # tag
                    html.Td(row[5], ),  # copy_text
                    html.Td(row[7], ),  # random1
                    html.Td(row[8], ),  # random2
                    html.Td(
                        dbc.NavLink("Annotate", href=f"/annotate={row[4]}", active="exact", ),
                    ),

                ]) for row in values],
            id='table-body'
        )
    ]

    print(f'[update_dataset_table]: : body')

    print(f'[update_dataset_table]: End')

    return [
        html.Div(
            [
                dbc.Input(id='search', type="search", style={'flex': '1'}, placeholder="Search"),
            ],
            style={
                'display': 'flex',
                'width': '100%',
                'gap': '10px',
            }
        ),

        html.Br(),

        html.Div(
            dbc.Table(table_header + table_body, id='dataset-table'),
            style={
                    'height': 'calc(75vh)',
                    'overflow': 'auto',
                  }
        ),

    ]


dataset_body_style = {
    'display': 'grid',
    'justify_content': 'center',
    'padding': '1rem',

}

dataset_layout = html.Div(
    id="dataset_layout",
    style={'display': 'none'}
)
