import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from datetime import date as dt

#imports backend
import server 

# Creates sidebar and main_content

sidebar =   dbc.Col(
                html.Div([
                        html.P("Select variables to display", className="lead"),
                        html.Br(),
                        dbc.FormGroup([
                            dbc.Label('Choose data to display'),
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
                                value='S',
                                
                            )
                        ]),  
                        dbc.FormGroup([
                            dbc.Label('Choose a date'),
                            html.Br(),
                            dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=dt(2020, 1, 1),
                                end_date_placeholder_text='Select a date!'
                            )
                        ]),
                        dbc.Button("Apply", id="submit-button-state",
                                color="primary", block=True)
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
mathjax = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML'
app.scripts.append_script({ 'external_url' : mathjax })

#setInterval("MathJax.Hub.Queue(['Typeset',MathJax.Hub])",1000)

app.layout = html.Div([

    html.H1("Covid19 Analysis 🇨🇱", style={'text-align': 'left'}),
    dcc.Tabs(id='tabs-chosen', value='tab-1', children=[
        dcc.Tab(label='National', value='tab-1'),
        dcc.Tab(label='Regional', value='tab-2'),
        dcc.Tab(label='SEIRD real data', value='tab-3'),
        dcc.Tab(label='SEIRD model', value='tab-4'),
        dcc.Tab(label='Docs', value='tab-5'),
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              Input('tabs-chosen', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            dbc.Row([ 
            dbc.Col(
                html.Div([
                        html.P("Select variables to display", className="lead"),
                        html.Br(),
                        dbc.FormGroup([
                            dbc.Label('Choose data to display'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Total cases', 'value': 'total'},
                                    {'label': 'Active cases', 'value': 'active'},
                                    {'label': 'Deaths', 'value': 'deaths'},
                                    {'label': 'Recovered', 'value': 'recovered'},
                                    {'label': 'Total PCR exams', 'value': 'pcr'},
                                ],
                                multi=True,
                                value='total',
                                
                            )
                        ]),
                        dbc.FormGroup([
                                dbc.Label("Additional setup"),
                                dbc.Checklist(
                                    options=[
                                        {"label": "per 1000 inhabitants", "value": 1},
                                        {"label": "logarithmic scale", "value": 2},
                                        {"label": "moving average", "value": 3, "disabled": True},
                                    ],
                                    value=[],
                                    id="switches-input",
                                    switch=True,
                                ),
                            ]),  
                        dbc.FormGroup([
                            dbc.Label('Choose a date'),
                            html.Br(),
                            dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=dt(2020, 1, 1),
                                end_date_placeholder_text='Select a date!'
                            )
                        ]),
                        dbc.Button("Apply", id="submit-button-state",
                                color="primary", block=True)
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
                ), main_content
            ])
        ])
    elif tab == 'tab-2':
        return html.Div([
             dbc.Row([ 
            dbc.Col(
                html.Div([
                        html.P("Select variables to display", className="lead"),
                        html.Br(),
                        dbc.FormGroup([
                            dbc.Label('Choose Regions'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Arica y Parinacota', 'value': 'arica'},
                                    {'label': 'Tarapacá', 'value': 'tarapaca'},
                                    {'label': 'Antofagasta', 'value': 'antofagasta'},
                                    {'label': 'Atacama', 'value': 'atacama'},
                                    {'label': 'Coquimbo', 'value': 'coquimbo'},
                                    {'label': 'Valparaíso', 'value': 'valparaiso'},
                                    {'label': 'Metropolitana', 'value': 'metropolitana'},
                                    {'label': 'O’Higgins', 'value': 'ohiggins'},
                                    {'label': 'Maule', 'value': 'maule'},
                                    {'label': 'Ñuble', 'value': 'nuble'},
                                    {'label': 'Biobío', 'value': 'biobio'},
                                    {'label': 'Araucanía', 'value': 'araucania'},
                                    {'label': 'Los Ríos', 'value': 'losrios'},
                                    {'label': 'Los Lagos', 'value': 'loslagos'},
                                    {'label': 'Aysén', 'value': 'aysen'},
                                    {'label': 'Magallanes', 'value': 'magallanes'},
                                ],
                                multi=True,
                                value='biobio',
                                
                            )
                        ]),  
                        dbc.FormGroup([
                            dbc.Label('Choose data to display'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Total cases', 'value': 'total'},
                                    {'label': 'Active cases', 'value': 'active'},
                                    {'label': 'Deaths', 'value': 'deaths'},
                                    {'label': 'Recovered', 'value': 'recovered'},
                                    {'label': 'Total PCR exams', 'value': 'pcr'},
                                ],
                                multi=False,
                                value='total',
                                
                            )
                        ]),  
                        dbc.FormGroup([
                                dbc.Label("Additional setup"),
                                dbc.Checklist(
                                    options=[
                                        {"label": "per 1000 inhabitants", "value": 1},
                                        {"label": "logarithmic scale", "value": 2},
                                        {"label": "moving average", "value": 3, "disabled": True},
                                    ],
                                    value=[],
                                    id="switches-input",
                                    switch=True,
                                ),
                            ]),
                        dbc.FormGroup([
                            dbc.Label('Choose a date'),
                            html.Br(),
                            dcc.DatePickerRange(
                                id='date-picker-range',
                                start_date=dt(2020, 1, 1),
                                end_date_placeholder_text='Select a date!'
                            )
                        ]),
                        dbc.Button("Apply", id="submit-button-state",
                                color="primary", block=True)
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
                ), main_content
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
            dbc.Col(
                html.Div([
                        html.P("Select variables to display", className="lead"),
                        html.Br(),
                        dbc.FormGroup([
                            dbc.Label('Date of first infection'),
                            html.Br(),
                            dcc.DatePickerSingle(
                                    day_size=39,  # how big the date picker appears
                                    display_format="DD.MM.YYYY",
                                    date='2020-01-01',
                                    id='initial_date',
                                    min_date_allowed=dt(2020, 12, 1),
                                    max_date_allowed=dt(2020, 5, 31),
                                    initial_visible_month=dt(2020, 1, 15),
                                    placeholder="test"
                            ),
                        ]),
                        dbc.FormGroup([
                                dbc.Label("Initial Cases"),
                                dbc.Input(
                                    id="initial_cases", type="number", placeholder="initial_cases",
                                    min=1, max=1_000_000, step=1, value=10,
                                )
                            ]),

                        dbc.FormGroup([
                                dbc.Label("Population"),
                                dbc.Input(
                                    id="population", type="number", placeholder="population",
                                    min=10_000, max=1_000_000_000, step=10_000, value=80_000_000,
                                )
                            ]),
                        dbc.FormGroup([
                                dbc.Label('ICU beds per 100k people'),
                                dbc.Input(
                                    id="icu_beds", type="number", placeholder="ICU Beds per 100k",
                                    min=0.0, max=100.0, step=0.1, value=34.0,
                                ),
                            ]),
                        dbc.FormGroup([
                                dbc.Label('Probability of going to ICU when infected (%)'),
                                html.Br(),
                                dcc.Slider(
                                    id='p_I_to_C',
                                    min=0.01,
                                    max=100.0,
                                    step=0.01,
                                    value=5.0,
                                    tooltip={'always_visible': True, "placement": "bottom"}
                                ),
                            ]),
                            dbc.FormGroup([
                                    dbc.Label('Probability of dying in ICU (%)'),
                                    dcc.Slider(
                                        id='p_C_to_D',
                                        min=0.01,
                                        max=100.0,
                                        step=0.01,
                                        value=50.0,
                                        tooltip={'always_visible': True, "placement": "bottom"}
                                    ),
                            ]),
                            dbc.FormGroup([
                                    dbc.Label('Reproduction rate R over time'),
                                    dcc.Slider(
                                        id='r0_slider',
                                        min=0.1,
                                        max=10,
                                        step=0.1,
                                        value=5,
                                        tooltip={'always_visible': True, "placement": "bottom"}
                                    ),
                            ]),
                            
                            dbc.Button("Apply", id="submit-button-state",
                                    color="primary", block=True)
    
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
                ),
            main_content
            ])
        ])
    elif tab == 'tab-5':
        return html.Div([
            dbc.Row([ 
            dbc.Col(# first, a jumbotron for the description and title
        dbc.Jumbotron(
            [
                dbc.Container(
                    [
                        html.H1("Compartmentalisation", className="display-3"),
                        html.P(
                            "SEIRD model explanation",
                            className="lead",
                        ),
                        html.Hr(className="my-2"),
                        dcc.Markdown('''
We separate population into several compartments, for example:
   - N: Total population
   - S: Susceptible (can still be infected, “healthy”)
   - E: Exposed (contracted the disease but is not yet infective) 
   - I: Infected (active cases)
   - R: Recovered (assuming were already infected and can't get infected again)
   - D: Dead (passed away from the disease)

Additional variables need to be used, such as:

 - &beta; (“beta”): the expected amount of people an infected person infects per day. For example, with a probability of 10% than 10 people will infect 1 person per day (10% &#183; 10 = 1)
 - D: delay in number of days that an infected person has to spread the disease
 - &gamma;: it's the rate of recovery, or the proportion of infected recovering per day &gamma;:1/D
 - R₀: this is the basic reproduction number R₀, which is the total number of people an infected person infects. R₀: &beta; &#183; D. Hence R₀: &beta; / &gamma;
 - &rho; rate at which people die (e.g. when it takes 6 days to die, ρ will be 1/6)
 - &alpha;: probability of going from infected to recovered and from infected to dead
                            '''
                                     )
                    ],
                    fluid=True,
                )
            ],
            fluid=True,
            className="jumbotron bg-white text-dark"
        ),
        ),
            dbc.Col(# first, a jumbotron for the description and title
        dbc.Jumbotron(
            [
                dbc.Container(
                    [
                        html.H1("Formulas", className="display-3"),
                        html.P(
                            "Calculates SEIRD model change over time",
                            className="lead",
                        ),
                        html.Hr(className="my-2"),
                        dcc.Markdown('''

### Susceptible: 
 
&part;S &frasl; &part;t  = -&beta; &#183; I &#183; S &frasl; N 

### Exposed: 
 
&part;E &frasl; &part;t = &beta; &#183; I &#183; S &frasl; N - &delta; &#183; E 

### Infectious: 

&part;I &frasl; &part;t = &delta;  &#183; E -(1-&alpha;) &#183; &gamma; &#183; I -&alpha;  &#183; &rho; &#183; I

### Recovered: 
 
&part;R &frasl; &part;t = (1-&alpha;) &#183; &gamma;  &#183; I 

### Dead: 

&part;R &frasl; &part;t = &alpha;  &#183; &rho;  &#183; I 

                            '''
                                     )
                    ],
                    fluid=True,
                )
            ],
            fluid=True,
            className="jumbotron bg-white text-dark"
        ),
        )
            ])
        ])
    
    
                    
        


##server = app.server
##app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)