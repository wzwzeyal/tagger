from dash import html, dcc
import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    dbc.Col(dbc.NavbarBrand("Tagger", className="ms-2")),
                    align="center",
                    className="g-0",
                ),
                style={"textDecoration": "none"},
            ),
            dbc.Row(
                [
                    dbc.NavbarToggler(id="navbar-toggler"),
                    dbc.Collapse(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Annotate", href='/annotate')),
                                dbc.NavItem(
                                    dbc.NavLink("Dataset", href='/dataset'),
                                    # add an auto margin after page 2 to
                                    # push later links to end of nav
                                    className="me-auto",
                                ),
                                dbc.NavItem(dbc.NavLink("Help", href='/help')),
                                dbc.NavItem(dbc.NavLink("About", href='/about')),
                            ],
                            # make sure nav takes up the full width for auto
                            # margin to get applied
                            className="w-100",
                        ),
                        id="navbar-collapse",
                        is_open=False,
                        navbar=True,
                    ),
                ],
                # the row should expand to fill the available horizontal space
                className="flex-grow-1",
            ),
        ],
        fluid=True,
    ),
    # dark=True,
    color="#eff2f5",
)