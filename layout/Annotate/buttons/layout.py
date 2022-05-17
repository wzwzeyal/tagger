from dash import html, dcc
import dash_bootstrap_components as dbc

from resources.strings import tag_button_names

buttons_list = [
    {"id": "button1", "text": "Button 1", "color": "black", "group": 1},
    {"id": "button2", "text": "Button 2", "color": "black", "group": 1},

    {"id": "button3", "text": "Button (3)", "color": "red", "group": 2},
    {"id": "Untagged", "text": "Remove", "color": "red", "group": 2},
]

buttons1 = []
buttons2 = []

for item in buttons_list:
    if item["group"] == 1:
        buttons1.append(
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
    elif item["group"] == 2:
        buttons2.append(
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
            buttons1,
            style={'height': '65%', }

        ),
        html.Div(
            buttons2,
            style={'height': '35%', }
        ),
    ],
    id="buttons_layout",
    style={
        'flex': 1
    }

)