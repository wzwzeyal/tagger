from dash import html, dcc
import dash_bootstrap_components as dbc

from resources.strings import tag_button_names

lst = []
for item in range(20):
    lst.append(
        dbc.Button(
            f'{tag_button_names[item]}',
            id=f'but{str(item)}',
            outline=True,
            # className="tag_button",
            style={
                # "width": "120px",
                "color": 'black',
                'border': 'groove',
                # "padding": "5px",
                "margin-right": 5,
                "margin-bottom": 3,
                "display": "inline",
                "border-radius": "0px"
                # "background-color": "white",
            },
        ),
    )

for item in range(20,30):
    lst.append(
        dbc.Button(
            f'{tag_button_names[item]}',
            id=f'but{str(item)}',
            outline=True,
            # className="tag_button",
            style={
                # "width": "120px",
                "color": 'red',
                'border': 'groove',
                # "padding": "5px",
                "margin-right": 5,
                "margin-bottom": 3,
                "display": "inline",
                "border-radius": "0px"
                # "background-color": "white",
            },
        ),
    )

buttons_layout = html.Div(
    [
        html.Div(
            lst[:20],
            style={'height': '65%', }

        ),
        html.Div(
            lst[20:],
            style={'height': '35%', }
        ),
    ],
    id="buttons_layout",
    style={
        'flex': 1
    }

)