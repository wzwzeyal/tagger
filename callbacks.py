from dash import Input, Output, no_update, callback_context, State
from app import app
from db import sql_update, sql_count, get_tag_id
from layout.annotate.buttons.layout import buttons_list
from layout.annotate.layout import annotate_layout_style
from layout.dataset.layout import dataset_body_style, update_datset_table
from layout.status.layout import status_layout_style
from resources.strings import tag_button_names
from utils import get_next_untagged

tag_buttons_input = []
# for item in range(len(tag_button_names)):
#     tag_buttons_input.append(
#         Input(f'but{str(item)}', 'n_clicks'))
for item in buttons_list:
    tag_buttons_input.append(
        Input(item["id"], 'n_clicks')
    )

tag_button_output = []
for item in buttons_list:
    tag_button_output.append(
        Output(item["id"], 'outline')
    )


@app.callback(
    Output("annotate_layout", "style"),
    Output("status_layout", "style"),
    Output("dataset_layout", "style"),
    Output("current-tag-id", "children"),
    Output("dataset_layout", "children"),

    Output('nof-tagged-texts', 'children'),
    Output('nof-total-texts', 'children'),
    Output('tag-left-progress', 'value'),

    tag_buttons_input,
    Input("url", "pathname"),  # -2
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
    untagged_data = get_next_untagged()

    nof_records = sql_count()
    nof_tags_left = sql_count("WHERE tag='Untagged'")  # len(data_df[data_df['tag'].str.contains("Untagged")])
    nof_tagged = nof_records - nof_tags_left
    percent_tagged = nof_tagged / nof_records

    if 'annotate' in pathname:

        # handle special cases
        if 'but' in button_id or 'Untagged' in button_id:
            # handle tag button click
            sql_update(button_id, current_tag_id)
            nof_records = sql_count()
            nof_tags_left = sql_count("WHERE tag='Untagged'")  # len(data_df[data_df['tag'].str.contains("Untagged")])
            nof_tagged = nof_records - nof_tags_left
            percent_tagged = nof_tagged / nof_records
            untagged_data = get_next_untagged()
            return (
                annotate_layout_style,
                status_layout_style,
                hidden_style,
                untagged_data['tag_id'],
                no_update,
                str(nof_tagged),
                str(nof_records),
                percent_tagged * 100
            )
        elif 'url' in button_id:
            if '=' in pathname:
                tag_id = pathname.split("=")[1]
                return (annotate_layout_style, status_layout_style, hidden_style, tag_id, no_update,
                        str(nof_tagged),
                        str(nof_records),
                        percent_tagged * 100)

        return (annotate_layout_style, status_layout_style, hidden_style, untagged_data['tag_id'], no_update,
                str(nof_tagged),
                str(nof_records),
                percent_tagged * 100)

    elif pathname == '/dataset':
        dataset = update_datset_table()
        return (hidden_style, hidden_style, dataset_body_style, no_update, dataset,
                no_update, no_update, no_update)

    else:
        print(f'[render_page_content]: unknown pathname: {pathname}')

    print(f'[render_page_content]: End')
    return no_update


@app.callback(
    Output('left-textarea-example', 'value'),
    Output('right-textarea-example', 'value'),
    Output('Text1', 'children'),
    Output('Text2', 'children'),
    Output('Text3', 'children'),

    tag_button_output,

    Input("current-tag-id", "children"),  # -1
)
def on_current_tag_id_change(current_tag_id):
    print(f'[on_current_tag_id_change]: current_tag_id: {current_tag_id}')
    current_tag = get_tag_id(current_tag_id)
    ctx = callback_context

    outputs = [True] * len(ctx.outputs_list);
    outputs[0] = current_tag["comment"]
    outputs[1] = current_tag["reverse"]
    outputs[2] = current_tag["copy_text"]
    outputs[3] = current_tag["random1"]
    outputs[4] = current_tag["random2"]

    tag_index = len(ctx.outputs_list) - 1 # Untagged

    for index, button in enumerate(buttons_list):
        if button['id'] == current_tag['tag']:
            tag_index = index
            break

    output_tag = 5 + tag_index
    if output_tag > len(outputs):
        output_tag = len(outputs) - 1

    outputs[output_tag] = False

    return outputs
