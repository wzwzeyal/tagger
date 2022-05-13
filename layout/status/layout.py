from dash import html, dcc
import dash_bootstrap_components as dbc

status_layout = html.Div(
    [
        # html.Div("Test", style={'border': 'solid',}),
        html.H4(
            [
                html.Span(
                    'Tagged texts: '
                ),
                html.B(
                    "45",
                    id="nof-tagged-texts",
                ),
                html.Span(
                    " out of "
                ),
                html.Span(
                    "1000",
                    id="nof-total-texts"
                ),
            ],
        ),

        dbc.Progress(
            id='tag-left-progress',
            value=12,
            style=
            {
                "flex": 0.95,
                'margin-left': '2rem',
                'background-color': '#ffffff',
                # 'height': 20,
                # 'border': 'solid',
                'height': '6px'
            },
        ),
    ],
    id="status_layout",
)
