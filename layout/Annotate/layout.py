from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.Annotate.buttons.layout import buttons_layout
from layout.Annotate.details.layout import details_layout

annotate_layout_style = {
    'display': 'flex',
    'height': '85%',
    'padding': '1rem',
}

annotate_layout = html.Div(
    [
        details_layout,
        html.Div(className="tag_spacer"),
        buttons_layout,
    ],
    id="annotate_layout",
    style=annotate_layout_style,
)