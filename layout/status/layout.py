from dash import html, dcc
import dash_bootstrap_components as dbc

status_layout = html.Div(
    [
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
                'background-color': '#5a5a5a',
                # 'height': 20,
                # 'border': 'solid',
                'height': '6px'
            },
        ),
    ],
    id="status_layout",
    style={
        'display': 'flex',
        'align-items': 'center',
        'padding': '1rem',
    }
)
