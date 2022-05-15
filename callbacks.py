from dash import Input, Output, no_update, callback_context, State
from app import app
from db import sql_update, sql_count, get_tag_id
from layout.Annotate.layout import annotate_layout_style
from layout.Dataset.layout import dataset_layout_style
from resources.strings import tag_button_names
from utils import get_next_untagged

tag_buttons_input = []
for item in range(len(tag_button_names)):
    tag_buttons_input.append(
        Input(f'but{str(item)}', 'n_clicks'))


@app.callback(
    Output("annotate_layout", "style"),
    Output("dataset_layout", "style"),
    Output("current-tag-id", "children"),

    tag_buttons_input,
    Input("url", "pathname"), # -2
    State("current-tag-id", "children")  # -1
)
def render_page_content(*args):
    print(f'[render_page_content]: Start')

    current_tag_id = args[-1]
    pathname = args[-2]

    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(f'[render_page_content]: button_id: {button_id}')

    print(f'[render_page_content]: pathname: {pathname}')
    hidden_style = {'display': 'none'}

    if 'annotate' in pathname:
        if button_id == "":
            # handle init
            # handle Annotate click
            untagged_data = get_next_untagged()
            return annotate_layout_style, hidden_style, untagged_data['tag_id']
        elif 'but' in button_id or 'Untagged' in button_id:
            # handle tag button click
            sql_update(button_id, current_tag_id)
            untagged_data = get_next_untagged()
            return annotate_layout_style, hidden_style, untagged_data['tag_id']
        elif 'url' in button_id:
            if '=' in pathname:
                tag_id = pathname.split("=")[1]
                return annotate_layout_style, hidden_style, tag_id

        # return no_update
        # if '=' in pathname:
        #     tag_id = pathname.split("=")[1]
        #     untagged_data = get_tag_id(tag_id)
        #
        #     if 'but' in button_id:
        #         print(f'[render_page_content]: button_id: {button_id}')
        #         sql_update(button_id, untagged_data['tag_id'])
        #         untagged_data = get_next_untagged()
        # else:
        #     if 'but' in button_id:
        #         print(f'[render_page_content]: button_id: {button_id}')
        #
        #     untagged_data = get_next_untagged()
        #
        # nof_records = sql_count()
        # nof_tags_left = sql_count("WHERE tag='Untagged'")  # len(data_df[data_df['tag'].str.contains("Untagged")])
        # nof_tagged = nof_records - nof_tags_left
        # percent_tagged = nof_tagged / nof_records
        # return (annotate_layout_style, hidden_style,
        #         untagged_data['comment'], untagged_data['reverse'],
        #         untagged_data['copy_text'],
        #         untagged_data['random1'],
        #         untagged_data['random2'],
        #         str(nof_tagged), str(nof_records), percent_tagged * 100,
        #         )



    elif pathname == '/dataset':
        return (hidden_style, dataset_layout_style, no_update)


    else:
        print(f'[render_page_content]: unknown pathname: {pathname}')

    print(f'[render_page_content]: End')
    return no_update

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

@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),

    # tag_buttons_input,
    Input("current-tag-id", "children"), # -1
)
def on_current_tag_id_change(current_tag_id):
    print(f'[on_current_tag_id_change]: current_tag_id: {current_tag_id}')
    current_tag = get_tag_id(current_tag_id)
    return (
        current_tag["comment"],
        current_tag["reverse"],
    )
