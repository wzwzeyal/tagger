from dash import html, dcc
import dash_bootstrap_components as dbc

from layout.Annotate.layout import annotate_layout
from layout.Dataset.layout import dataset_layout
from layout.Navbar.layout import navbar
from layout.header.layout import header_layout
from layout.status.layout import status_layout
from layout.table.layout import table_layout
from layout.tag.layout import tag_layout

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
    # "background-color": "red",
}

CONTENT_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "right": 0,
    "margin-left": "14rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",
    "background-color": "#eff2f5",
}


sidebar = html.Div(
    [
        html.H2("Tagger", className="display-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Annotate", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
            id="dbc_nav"
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)


def create_layout():
    layout = html.Div(
        [
            dcc.Location(id="url", pathname="/annotate"),

            html.Div(id="current-row"),

            navbar,

            # sidebar,

            annotate_layout,

            dataset_layout,

            status_layout,
            #
            # table_layout,
        ],
        id='body',
    )

    return layout
