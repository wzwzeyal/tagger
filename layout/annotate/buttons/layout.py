from dash import html, dcc
import dash_bootstrap_components as dbc
from collections import defaultdict

from resources.strings import tag_button_names

buttons_dict = {
    'button1': {'color': 'black', 'group': 'group1'},
    'button2': {'color': 'black', 'group': 'group1'},
    'button3': {'color': 'black', 'group': 'group1'},
    'button4': {'color': 'black', 'group': 'group1'},
    'button5': {'color': 'black', 'group': 'group1'},
    'button6': {'color': 'black', 'group': 'group2'},
    'Untagged': {'color': 'black', 'group': 'group2'},
}

buttons = defaultdict()

for button_item in buttons_dict:
    group = buttons_dict[button_item]["group"]
    color = buttons_dict[button_item]["color"]
    if group not in buttons.keys():
        buttons[group] = []

    buttons[group].append(
        dbc.Button(
            button_item,
            id=button_item,
            outline=True,

            style={
                "color": color,
                'border': 'groove',
                "margin-right": 5,
                "margin-bottom": 3,
                "display": "inline",
                "border-radius": "0px"

            },
        )
    )

buttons_layout = html.Div(
    [
        html.Div(
            buttons['group1'],
            style={'height': '65%', }

        ),
        html.Div(
            buttons['group2'],
            style={'height': '35%', }
        ),
    ],
    id="buttons_layout",
    style={
        'flex': 1
    }

)
