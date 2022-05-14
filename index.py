import dash_bootstrap_components as dbc
import dash
import callbacks

from app import app
from app import server
import dash_bootstrap_components as dbc
import pandas as pd
# sudo kill $(sudo lsof -t -i:8050)
from dash import Dash, dcc, html
from dash import Input, Output, no_update, callback_context, State
from flask import Flask
from sqlalchemy import create_engine, text

from layout.app_layout import create_layout

app.layout = create_layout()

if __name__ == '__main__':
    app.run_server(debug=True)
