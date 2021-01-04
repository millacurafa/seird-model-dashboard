import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from datetime import date

#imports backend
import server 

# Creates sidebar and main_content

sidebar =   dbc.Col(
                html.Div([
                        html.P("Select variables to display", className="lead"),
                        html.Br(),
                        dcc.Dropdown(
                            options=[
                                {'label': 'Susceptible', 'value': 'S'},
                                {'label': 'Exposed', 'value': 'E'},
                                {'label': 'Infectious', 'value': 'I'},
                                {'label': 'Recovered', 'value': 'R'},
                                {'label': 'Dead', 'value': 'D'},
                            ],
                            multi=True,
                            value='MTL',
                            
                        ),
                        html.Br(),
                        dcc.DatePickerRange(
                            id='date-picker-range',
                            start_date=date(2020, 1, 1),
                            end_date_placeholder_text='Select a date!'
                        )
                    ]),
                    width=3,
                    style= {
                            "margin-left": "2rem",
                            "padding": "2rem 1rem",
                            "background-color": "#f8f9fa",
                            "left":0,
                            "top": 0,
                            "bottom": 0,
                        }
                )
            
main_content = dbc.Col(html.Div(dcc.Graph(id='time-series')), 
                        width=8,
                        style = {
                            "margin-left": "4rem",
                            "margin-right": "2rem",
                            "padding": "2rem 1rem",
                        }
                )
                   

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
            dbc.Row([ 
            sidebar, main_content
            ])
        ])
    elif tab == 'tab-2':
        return html.Div([
            dbc.Row([ 
            sidebar, main_content
            ])
        ])
    elif tab == 'tab-3':
        return html.Div([
            dbc.Row([ 
            sidebar, main_content
            ])
        ])
    elif tab == 'tab-4':
        return html.Div([
            dbc.Row([ 
            sidebar, main_content
            ])
        ])


##server = app.server
##app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)