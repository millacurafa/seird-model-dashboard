import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import date as dt
import server as sv
# Defines functions

#Figs to display

fig1 = sv.px.line(sv.df['Casos totales']).update_layout(title= "National cases",
                    yaxis_title='Number of National cases',
                    xaxis_title='Date')

fig2 = sv.px.line(sv.df_region_current_bypop['bypop']
    ).update_layout(title= "Regional cases",
                    yaxis_title='Number of Regional cases',
                    xaxis_title='Date')
fig3 = sv.px.line(sv.df_seird
    ).update_layout(title='SEIRD model real data',
                    yaxis_title='SEIRD cases',
                    xaxis_title='Date')

fig4 = sv.plotlyseirdgo(sv.t, sv.S, sv.E, sv.I, sv.R, sv.D)


# Main content one
main_content_one = dbc.Col([
    dbc.Row([
        dbc.Col(
            dbc.FormGroup([
                                dbc.Label("Additional setup"),
                                html.Br(),
                                dbc.Checklist(
                                    options=[
                                        {"label": "per 1000 inhabitants", "value": 1},
                                        {"label": "logarithmic scale", "value": 2},
                                        {"label": "moving average", "value": 4, "disabled": False},
                                    ],
                                    value=[],
                                    id="national_switches_input",
                                    switch=True,
                                ),
                            ]),style = {'display': 'inline-block'}),
    ]),
    dbc.Row(dbc.Col(dcc.Graph(id='time_series_one', figure=fig1),width=12))],
    width=8,
    style = {   "margin-left": "4rem",
                "margin-right": "2rem",
                "padding": "2rem 1rem"})
# Main content two
main_content_two = dbc.Col([  
    dbc.Row([ 
        dbc.Col(
        dbc.FormGroup(
            [
                dbc.Label("Additional setup"),
                dbc.Checklist(
                                    options=[
                                        {"label": "per 1000 inhabitants", "value": 1},
                                        {"label": "logarithmic scale", "value": 2},
                                        {"label": "moving average", "value": 3, "disabled": True},
                                    ],
                                    value=[],
                                #    labelStyle={'display': 'inline-block'},
                                    id="regional_switches_input",
                                    switch=True,
                                    
                                ),
                            ],style = {'display': 'inline-block'})
        ),
        dbc.Col(
            
                        dbc.FormGroup([
                            dbc.Label('Choose Regions'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Arica y Parinacota', 'value': 'Arica y Parinacota'},
                                    {'label': 'Tarapacá', 'value': 'Tarapaca'},
                                    {'label': 'Antofagasta', 'value': 'Antofagasta'},
                                    {'label': 'Atacama', 'value': 'Atacama'},
                                    {'label': 'Coquimbo', 'value': 'Coquimbo'},
                                    {'label': 'Valparaíso', 'value': 'Valparaiso'},
                                    {'label': 'Metropolitana', 'value': 'Metropolitana'},
                                    {'label': 'O’Higgins', 'value': 'Del Libertador General Bernardo O’Higgins'},
                                    {'label': 'Maule', 'value': 'Maule'},
                                    {'label': 'Ñuble', 'value': 'Nuble'},
                                    {'label': 'Biobío', 'value': 'Biobio'},
                                    {'label': 'Araucanía', 'value': 'La Araucania'},
                                    {'label': 'Los Ríos', 'value': 'Los Rios'},
                                    {'label': 'Los Lagos', 'value': 'Los Lagos'},
                                    {'label': 'Aysén', 'value': 'Aysen'},
                                    {'label': 'Magallanes', 'value': 'Magallanes y la Antartica'},
                                ],
                                multi=True,
                                value=['Arica y Parinacota',
                                    'Tarapaca',
                                    'Antofagasta',
                                    'Atacama',
                                    'Coquimbo',
                                    'Valparaiso',
                                    'Metropolitana',
                                    'Del Libertador General Bernardo O’Higgins',
                                    'Maule',
                                    'Nuble',
                                    'Biobio',
                                    'La Araucania',
                                    'Los Rios',
                                    'Los Lagos',
                                    'Aysen',
                                    'Magallanes y la Antartica'
                                ],
                                id='regional_dropdown'
                                
                            )
                        ]), width=8  
        )
                            
    ]),
        dbc.Row(dbc.Col(dcc.Graph(id='time_series_two',figure=fig2),width=12))],
    width=8,
    style = {
             "margin-left": "4rem",
            "margin-right": "2rem",
            "padding": "2rem 1rem",
            })
## Main content three
main_content_three = dbc.Col([  

    dbc.Row(dbc.Col(dcc.Graph(id='time_series_three',figure=fig3),width=12))
    ], 
    width=8,
    style = {
    "margin-left": "4rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    })  
## Main content four
main_content_four = dbc.Col([
    dbc.Row([
        
        dbc.Col(
            dbc.FormGroup([
                            dbc.Label('Choose a Region'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Arica y Parinacota', 'value': 'Arica y Parinacota'},
                                    {'label': 'Tarapacá', 'value': 'Tarapaca'},
                                    {'label': 'Antofagasta', 'value': 'Antofagasta'},
                                    {'label': 'Atacama', 'value': 'Atacama'},
                                    {'label': 'Coquimbo', 'value': 'Coquimbo'},
                                    {'label': 'Valparaíso', 'value': 'Valparaiso'},
                                    {'label': 'Metropolitana', 'value': 'Metropolitana'},
                                    {'label': 'O’Higgins', 'value': 'Del Libertador General Bernardo O’Higgins'},
                                    {'label': 'Maule', 'value': 'Maule'},
                                    {'label': 'Ñuble', 'value': 'Nuble'},
                                    {'label': 'Biobío', 'value': 'Biobio'},
                                    {'label': 'Araucanía', 'value': 'La Araucania'},
                                    {'label': 'Los Ríos', 'value': 'Los Rios'},
                                    {'label': 'Los Lagos', 'value': 'Los Lagos'},
                                    {'label': 'Aysén', 'value': 'Aysen'},
                                    {'label': 'Magallanes', 'value': 'Magallanes y la Antartica'},
                                ],
                                multi=False,
                                value='Valparaiso',
                                id='seird_regional_dropdown'
                                
                            )
                        ]), width=4
        ), 
        dbc.Col(
            dbc.FormGroup([
                            dbc.Label('Choose a City'),
                            html.Br(),
                            dcc.Dropdown(
                                options= [{'label': 'Zapallar', 'value': 'Zapallar'}],
                                multi=False,
                                value=['Zapallar'],
                                id='seird_city_dropdown'
                                
                            )
                        ]), width=4 
        ),
        
        dbc.Col(
            dbc.FormGroup([
                dbc.Label('Date of first infection'),
                    html.Br(),
                    dcc.DatePickerSingle(
                        day_size=30,  # how big the date picker appears
                        display_format="YYYY-MM-DD",
                        date='2020-01-01',
                        min_date_allowed=dt(2020, 1, 1),
                        max_date_allowed=dt.today(),
                        initial_visible_month=dt(2020, 1, 15),
                        placeholder="test",
                        id='seirdmo_daypicker',
                    )
            ]), width=4    
        ),
    ]),


dbc.Row(dbc.Col(dcc.Graph(id='time_series_four',figure=fig4), width=12))], 
            width=8,
            style = {
                            "margin-left": "4rem",
                            "margin-right": "2rem",
                            "padding": "2rem 1rem",
            })                      
## Tab 1

tab_1 = dbc.Row([ 
            dbc.Col(
                html.Div([
                        html.P("Select variables to display", className="lead"),
                        html.Br(),
                        dbc.FormGroup([
                            dbc.Label('Choose data to display'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Total cases', 'value': 'Casos totales'},
                                    {'label': 'Daily cases', 'value': 'Casos nuevos totales'},
                                    {'label': 'Active cases', 'value': 'Casos activos'},
                                    {'label': 'Deaths', 'value': 'Fallecidos'},
                                    {'label': 'Recovered', 'value': 'recovered'},
                                 #   {'label': 'Total PCR exams', 'value': 'pcr'},
                                ],
                                multi=True,
                                value='Casos totales',
                                id= 'national_dropdown',
                            )
                        ]),  
                        dbc.FormGroup([
                            dbc.Label('Choose a date'),
                            html.Br(),
                            dcc.DatePickerRange(
                                id='national_datepicker',
                                start_date=dt(2020, 1, 1),
                                end_date=dt.today(),
                                display_format="YYYY-MM-DD",
                                end_date_placeholder_text='Select a date!',
                                day_size = 30
                            )
                        ]),
                        dbc.Button("Apply", id="submit_button_state_one",
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
                ), main_content_one
            ])

## Tab 2

tab_2 = dbc.Row([ 
            dbc.Col(
                html.Div([

                        dbc.FormGroup([
                            dbc.Label('Choose a date'),
                            html.Br(),
                            dcc.DatePickerRange(
                                start_date=dt(2020, 1, 1),
                                end_date=dt.today(),
                                display_format="YYYY-MM-DD",
                                end_date_placeholder_text='Select a date!',
                                id='regional_datepicker',
                                day_size = 30
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
                                    {'label': 'Critical cases', 'value': 'uci'},
                                    {'label': 'Total PCR exams', 'value': 'pcr'},
                                ],
                                multi=False,
                                value='active',
                                id='regional_cases'
                                
                            )
                        ]), 
                        
                        dbc.Button("Apply", id="submit_button_state_two",
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
            
            main_content_two
            ]),

## Tab 3

tab_3 = dbc.Row([ 
            dbc.Col(
                html.Div([
                        dbc.FormGroup([
                            dbc.Label('Choose data to display'),
                            html.Br(),
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Susceptible', 'value': 'Susceptible'},
                                    {'label': 'Exposed', 'value': 'Exposed'},
                                    {'label': 'Infectious', 'value': 'Infectious'},
                                    {'label': 'Recovered', 'value': 'Recovered'},
                                    {'label': 'Dead', 'value': 'Dead'},
                                ],
                                multi=True,
                                value=['Susceptible','Exposed','Infectious','Recovered','Dead'],
                                id="seird_dropdown",
                                
                            )
                        ]),  
                        dbc.FormGroup([
                            dbc.Label('Choose a date'),
                            html.Br(),
                            dcc.DatePickerRange(
                                start_date=dt(2020, 3, 2),
                                end_date=dt.today(),
                                display_format="YYYY-MM-DD",
                                end_date_placeholder_text='Select a date!',
                                id='seird_datepicker',
                                day_size = 30
                            )
                        ]),
                        dbc.Button("Apply", id="submit_button_state_three",
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
                main_content_three
])
## Tab 4

tab_4 = dbc.Row([ 
            dbc.Col(
                html.Div([
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Days to predict"),
                                dbc.Input(
                                    id="seirdmo_days_today", type="number", placeholder="initial_cases",
                                    min=0, max=1_000, step=1, value=700,
                                )])
                        ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Initial Cases"),
                                dbc.Input(
                                    id="seirdmo_initial_cases", type="number", placeholder="initial_cases",
                                    min=0, max=1_000_000, step=1, value=10,
                                )]),
                            dbc.Col([
                                dbc.Label("Initial Deaths"),
                                dbc.Input(
                                    id="seirdmo_initial_deaths", type="number", placeholder="initial_deaths",
                                    min=0, max=1_000_000, step=1, value=0,
                                )]),    
                            ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label("Initial Exposed"),
                                dbc.Input(
                                    id="seirdmo_initial_exposed", type="number", placeholder="initial_exposed",
                                    min=0, max=1_000_000, step=1, value=0,
                                )]),
                            dbc.Col([
                                dbc.Label("Initial Recovered"),
                                dbc.Input(
                                    id="seirdmo_initial_recovered", type="number", placeholder="initial_recovered",
                                    min=0, max=1_000_000, step=1, value=0,
                                )]),    
                            ]),
                        dbc.FormGroup([
                                dbc.Label("Population"),
                                dbc.Input(
                                    id="seirdmo_population", type="number", placeholder="population",
                                    min=1_000, max=1_000_000_000, step=1_000, value=18_300_000,
                                )
                            ]),
                        dbc.Row([
                            dbc.Col([
                                dbc.Label('ICU beds per 1K people'),
                                dbc.Input(
                                    id="seirdmo_icu_beds", type="number", placeholder="ICU Beds per 1000",
                                    min=0.0, max=100.0, step=0.1, value=34.0,
                                ),
                            ]),
                            dbc.Col([
                                dbc.Label('PCR tests per 1K people'),
                                dbc.Input(
                                    id="seirdmo_pcr", type="number", placeholder="PCR per 1000",
                                    min=0.0, max=100.0, step=0.1, value=34.0,
                                ),
                            ]),
                        ]),
                        dbc.FormGroup([
                                dbc.Label('Probability of going to ICU when infected (%)'),
                                html.Br(),
                                dcc.Slider(
                                    id='seirdmo_p_I_to_C',
                                    min=0.1,
                                    max=100.0,
                                    step=0.1,
                                    value=20.0,
                                    tooltip={'always_visible': False, "placement": "bottom"}
                                ),
                            ]),
                            dbc.FormGroup([
                                    dbc.Label('Probability of dying in ICU (%)'),
                                    dcc.Slider(
                                        id='seirdmo_p_C_to_D',
                                        min=0.1,
                                        max=100.0,
                                        step=0.1,
                                        value=5.0,
                                        tooltip={'always_visible': False, "placement": "bottom"}
                                    ),
                            ]),
                            dbc.FormGroup([
                                    dbc.Label('Reproduction rate (R) over time'),
                                    dcc.Slider(
                                        id='seirdmo_r0_slider',
                                        min=0.1,
                                        max=10.0,
                                        step=0.1,
                                        value=2.0,
                                        tooltip={'always_visible': False, "placement": "bottom"}
                                    ),
                            ]),
                            
                            dbc.Button("Apply", id="submit_button_state_four",
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
            main_content_four
            ])

## Tab 5

tab_5 = dbc.Row([ 
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
            