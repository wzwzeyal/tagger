import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc, dash_table

data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
data_df.sort_values(by='tag_id', inplace=True)
data_df.set_index('tag_id', inplace=True, drop=False)


# tagged_df = data_df[~data_df['tag'].str.contains('Untagged')]
tagged_df = data_df.copy()

print(tagged_df.columns)
table_header = [
    html.Tr([html.Th("ID"), # 4
             html.Th("Left", ), # 1
             html.Th("Right"), # 6
             html.Th("Tag"), # 6
             html.Th("Text1"), # 7
             html.Th("Text2"), # 8
             html.Th("Text3"), # 9
             ])
]

col_style = {'max-width': '10px', 'overflow': 'hidden', 'white-space': 'nowrap'}

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

for row in tagged_df:
    html.Td()
    table_body.append(
        html.Tr()
    )

dataset_layout_style = {
    'max-height': 'calc(92vh)',
    'padding': '1rem',
}

dataset_layout = html.Div(
    [

        dbc.Table(

            table_header + table_body,  #striped=True,
            bordered=True,
            style={'overflow-x': 'auto'}),


        # dbc.Table.from_dataframe(tagged_df, striped=True, bordered=True, hover=True),

        # dash_table.DataTable(
        #     tagged_df.to_dict('records'),
        #     # [{"name": i, "id": i} for i in tag_data_df.columns],
        #     id='records-data-table',
        #     columns=
        #     [
        #         dict(name='Tag', id='tag'),
        #         dict(name='Copy', id='copy_text', ),
        #         dict(name="random2", id="random2", ),
        #         dict(name="random1", id="random1", ),
        #         dict(name='Right Text', id='reverse', ),
        #         dict(name='Left Text', id='comment'),
        #         dict(name='markdown Id', id='markdown', type='text', presentation='markdown'),
        #     ],
        #     # page_current=0,
        #     # page_size=10,
        #     # page_action='native',
        #     style_table={
        #         'max-height': 'calc(92vh)',
        #         'overflowY': 'auto',
        #     },
        #     sort_action='native',
        #     filter_action='native',
        #     editable=True,
        #     style_data=
        #     {
        #         'maxWidth': '150px',
        #         'overflow': 'hidden',
        #         'textOverflow': 'ellipsis',
        #     },
        #     style_data_conditional=[
        #         {
        #             'if': {
        #                 'state': 'active'  # 'active' | 'selected'
        #             },
        #             'backgroundColor': 'white'
        #         },
        #         {
        #             'if': {
        #                 'state': 'selected'  # 'active' | 'selected'
        #             },
        #             'backgroundColor': 'white'
        #         },
        #     ],
        # ),

    ],

    className="base_layout",
    id="dataset_layout",
    style={'display': 'none'}

    # style=
    # {
    #     'position': 'absolute',
    #     'left': 10,
    # },
)
