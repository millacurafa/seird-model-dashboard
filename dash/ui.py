import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#import dash_table
#import mydcc
from datetime import datetime as dt

#imports backend
import server as sv


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)