from dash import html, dcc
import dash_bootstrap_components as dbc

details_layout = html.Div(
    [
        dbc.Textarea(id="left-textarea-example", placeholder="1", readonly=True,
                     style={'height': '45%', 'direction': 'rtl', }
                     ),
        html.Div(style={'height': '1rem'}),
        dbc.Textarea(id="right-textarea-example", placeholder="1", readonly=True,
                     style={'height': '45%', 'direction': 'rtl'}
                     ),
        html.Div(style={'height': '1rem'}),
        html.Div(
            [
                html.Div(
                    [
                        html.Span(
                            "Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1",
                            id="Text1",
                        ),
                        dcc.Clipboard(
                            target_id="Text1",
                            style={
                                "position": "absolute",
                                "top": 2,
                                "right": 4,
                                "fontSize": 20,
                            },
                        ),
                    ],
                    className="flex-1-border",
                    style={"position": "relative"}),
                html.Span("Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1", id="Text2", className="flex-1-border", ),
                html.Span("Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1Text1", id="Text3", className="flex-1-border", ),

            ],
            id="row_additional_data",
            style={
                'display': 'flex',
                'gap': '1rem',
                'height': '7%',
                'align-content': 'start',
            }
        ),

    ],
    id="details_layout",
    style={
        'flex': 3,
    }
)
