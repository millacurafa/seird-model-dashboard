import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#from server import demoplot
from dash.dependencies import Input, Output
from datetime import date


#import dash_table
#import mydcc
#from datetime import datetime as dt

#imports backend
##from tabs import sidepanel, tab1, tab2
import pandas as pd
import numpy  as np
import plotly.express as px
from scipy.integrate import odeint

#Imports national data

df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales_T.csv',
                error_bad_lines=False
                 )

df= df.set_index('Fecha')

#Checking for data correlations

correlations = df[['Casos totales',
                   'Casos recuperados',
                   'Fallecidos',
                   'Casos activos',
                   'Casos nuevos totales',
                  'Casos nuevos con sintomas',
                  'Casos nuevos sin sintomas']].corr()
                   

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

sidebar = html.Div([
        id="page-sidebar",
        html.P(
            "Select variables to display", className="lead"
        ),
        dbc.Row(
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            multi=True,
            value='MTL',
            
        )),
        dbc.Row(dcc.DatePickerRange(
            id='date-picker-range',
            start_date=date(1997, 5, 3),
            end_date_placeholder_text='Select a date!'
        ))      
    ],
)

content = html.Div(id="page-content")

app.layout = html.Div([

    html.H1("Analisis Covid19 🇨🇱", style={'text-align': 'left'}),

    
    dcc.Tabs(id='tabs-chosen', value='tab-1', children=[
        dcc.Tab(label='National', value='tab-1'),
        dcc.Tab(label='Regional', value='tab-2'),
        dcc.Tab(label='SEIRD real data', value='tab-3'),
        dcc.Tab(label='SEIRD model', value='tab-4'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs-chosen', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            sidebar,
            content
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.Graph(px.imshow(correlations))
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3')
        ])
    elif tab == 'tab-4':
        return html.Div([
        html.H3('Tab content 4')
        ])


##server = app.server
##app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)