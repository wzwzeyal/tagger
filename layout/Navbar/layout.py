from dash import html, dcc
import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    [
        html.H2("Tagger", style={"padding-left": "1rem"}),
        dbc.NavLink("Annotate", href='/annotate', style={"margin-left": "2rem", }),
        dbc.NavLink("Dataset", href='/dataset', ),
    ],
    id="Navbar",
)
