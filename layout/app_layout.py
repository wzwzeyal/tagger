from dash import html, dcc
import dash_bootstrap_components as dbc

from db import sql_select_next
from layout.annotate.layout import annotate_layout
from layout.dataset.layout import dataset_layout
from layout.Navbar.layout import navbar
from layout.header.layout import header_layout
from layout.status.layout import status_layout


def create_layout():
    layout = html.Div(
        [
            dcc.Location(id="url", pathname=f"/annotate"),

            html.Div(id="current-tag-id", style={'display': 'none'}),

            navbar,

            annotate_layout,

            dataset_layout,

            status_layout,
        ],
        id='body',
    )

    return layout
