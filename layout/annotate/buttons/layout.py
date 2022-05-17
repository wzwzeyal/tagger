from dash import html, dcc
import dash_bootstrap_components as dbc
from collections import defaultdict

from resources.strings import tag_button_names

buttons_list = [
    {"id": "button1", "text": "Short", "color": "black", "group": 'group1'},
    {"id": "button2", "text": "Long Button", "color": "black", "group": 'group1'},
    {"id": "button3", "text": "Very Long Button Button", "color": "black", "group": 'group1'},
    {"id": "button4", "text": "Button 4", "color": "black", "group": 'group1'},
    {"id": "button5", "text": "Button 4", "color": "black", "group": 'group1'},
    {"id": "button6", "text": "Button 6", "color": "black", "group": 'group1'},

    {"id": "button7", "text": "Button (3)", "color": "red", "group": 'group2'},
    {"id": "Untagged", "text": "Unknown", "color": "red", "group": 'group2'},
]

buttons = defaultdict()

for item in buttons_list:
    if not item["group"] in buttons.keys():
        buttons[item["group"]] = []

    buttons[item["group"]].append(
        dbc.Button(
            item["text"],
            id=f'{item["id"]}',
            outline=True,

            style={
                "color": item["color"],
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
