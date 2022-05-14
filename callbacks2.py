from app import app

import dash_bootstrap_components as dbc
import pandas as pd
# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash
from dash import Input, Output, no_update, callback_context, State
from flask import Flask
from sqlalchemy import create_engine, text

from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.header.layout import header_layout
from layout.status.layout import status_layout
from layout.table.layout import table_layout
from layout.tag.layout import tag_layout
from resources.strings import tag_button_names

engine = create_engine('postgresql://postgres:postgres@localhost/test', echo=True)

tag_buttons_input = []
for item in range(len(tag_button_names)):
    tag_buttons_input.append(
        Input(f'but{str(item)}', 'n_clicks'))


# @app.callback(
#     Output('nof-tagged-texts', 'children'),
#     Output('nof-total-texts', 'children'),
#     Output('tag-left-progress', 'value'),
#     Input('records-data-table', 'data'),
# )
# def on_data_change(_):
#     print("on_data_change")
#     return no_update
#     data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
#     # return no_update
#     print(f'[on_data_change]: Start')
#     nof_records = sql_count()
#     nof_tags_left = sql_count("WHERE tag='Untagged'")  # len(data_df[data_df['tag'].str.contains("Untagged")])
#     nof_tagged = nof_records - nof_tags_left
#     percent_tagged = nof_tagged / nof_records
#
#     print(f'[on_data_change]: nof_tags_left: {nof_tags_left}')
#     print(f'[on_data_change]: End')
#     return str(nof_tagged), str(nof_records), percent_tagged * 100


def get_next_untagged():
    res = sql_select_next()

    return res


# @app.callback(
#     Output('left-textarea-example', 'value'),
#     Output('right-textarea-example', 'value'),
#     tag_buttons_input,
# )
# def on_button_click(*args):
#     print(f'[on_button_click]: Start')
#
#     data_df = pd.read_sql_table('test_tsv', "postgresql://postgres:postgres@localhost/test")
#     data_df.sort_values(by='tag_id', inplace=True)
#     data_df.set_index('tag_id', inplace=True, drop=False)
#
#     ctx = callback_context
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     print(f'[on_button_click]: button_id: {button_id}')
#
#     next_untagged = get_next_untagged()
#     tagged_data = data_df[~data_df['tag'].str.contains('Untagged')]
#
#     output_res = no_update
#
#     # handle initial state
#     if button_id == "":
#         print(f'[on_button_click]: initial state')
#         output_res = (
#             next_untagged['comment'],
#             next_untagged['reverse'],
#         )
#         return output_res
#
#     if 'but' in button_id or 'Untagged' in button_id:
#         # change current tag (init or not selected)
#         output_res = update_details_tag(data_df, button_id, next_untagged)
#
#     return output_res


def update_text_on_switching_active_cell(active_cell, data):
    print(f'[update_text_on_switching_active_cell]: Start')
    output_res = no_update
    if active_cell is None:
        return output_res

    selected_row = active_cell['row_id']
    if selected_row < len(data):
        row = data[selected_row]
        output_res = (row['comment'], row['reverse'],
                      # str(row['copy_text']),
                      no_update, no_update,)

    print(f'[update_text_on_switching_active_cell]: End')
    return output_res


def update_active_cell_tag(data_df, active_cell, button_id, data, next_untagged):
    print(f'[update_active_cell_tag]: Start')
    selected_row = active_cell['row_id']
    print(f'[on_tag_click]: selected_row: {selected_row}')
    row = data[selected_row]
    tag_table_id = row['tag_id']
    data_df.at[tag_table_id, 'tag'] = button_id
    sql_update(button_id, tag_table_id)
    tagged_data = data_df[~data_df['tag'].str.contains('Untagged')]
    output_res = (next_untagged['comment'], next_untagged['reverse'],
                  # str(next_untagged['copy_text']),
                  tagged_data.to_dict('records'),
                  None,)
    print(f'[update_active_cell_tag]: End')
    return output_res


def update_details_tag(data_df, button_id, next_untagged):
    print(f'[update_details_tag]: Start')
    tag_table_id = next_untagged['tag_id']
    data_df.at[tag_table_id, 'tag'] = button_id
    sql_update(button_id, tag_table_id)
    next_untagged = get_next_untagged()
    output_res = (next_untagged['comment'], next_untagged['reverse'], )

    print(f'[update_details_tag]: End')
    return output_res


def sql_select_next():
    with engine.begin() as connection:
        tbl_name = 'test_tsv'
        sql_str = f"SELECT * from {tbl_name} WHERE tag = 'Untagged' LIMIT 1"
        res = pd.read_sql_query(text(sql_str), con=connection)
        # res = connection.execute(text(sql_str))
    return res.iloc[0]


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

        print(f'[sql_update]: res: {res}')
    print(f'[sql_update]: End')


# @app.callback(
#     Output("tag_layout", "style"),
#     Output("status_layout", "style"),
#     Output("table_layout", "style"),
#     [Input("url", "pathname")]
# )
# def render_page_content(pathname):
#     print(f'[render_page_content]: Start')
#     print(f'[render_page_content]: pathname: {pathname}')
#
#     hidden_layout = {'display': 'none'}
#     visible_layout = {'margin-left': '14rem'}
#     visible_tag = {
#
#         'display': 'flex',
#         'background-color':  '#ffffff',
#         'height': '95%',
#         'padding': '1rem',
#         'margin-left': '14rem',
#     }
#     if pathname == "/":
#         return visible_tag, visible_layout, hidden_layout
#
#     elif pathname == "/page-1":
#         return hidden_layout, hidden_layout, visible_layout
#
#     elif "tag" in pathname:
#         tag_id = pathname.split("=")[1]
#         print(tag_id)
#         return visible_tag, hidden_layout, hidden_layout
#
#     # If the user tries to reach a different page, return a 404 message
#     return html.Div(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ], hidden_layout, hidden_layout, hidden_layout
#     )

