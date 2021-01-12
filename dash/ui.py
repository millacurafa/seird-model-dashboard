import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import tabs as tb
# imports backend
import server as sv

# Uses bootstrap stylesheet
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

##Creates layout

app.layout = html.Div([
    html.Div([html.Img(src='/static/images/databio_logo.svg',
        style = {'display': 'inline', 'width': '50%', 'max-width': '8rem'}),
        html.H1("Covid19 Analysis 🇨🇱", style={'text-align': 'center', 'color':'white'}), 
        html.P(['made with ❤ by ', html.A('millacurafa', href='https://github.com/millacurafa', style={'color':'white'})],
        style={'text-align': 'center', 'color':'white'}),
        ], className = 'navbar navbar-primary bg-dark'),
    dcc.Tabs(id='tabs_chosen', value='tab-1', children=[
        dcc.Tab(label='National', value='tab-1'),
        dcc.Tab(label='Regional', value='tab-2'),
        dcc.Tab(label='SEIRD real data', value='tab-3'),
        dcc.Tab(label='SEIRD model', value='tab-4'),
        dcc.Tab(label='Docs', value='tab-5'),
    ]),
    html.Div(id='tabs_content')
])

##Generates callbacks
@app.callback(        
    Output('tabs_content', 'children'),
    Input('tabs_chosen', 'value')
)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div(
            tb.tab_1
        )
    elif tab == 'tab-2':
        return html.Div(
            tb.tab_2
        )
    elif tab == 'tab-3':
        return html.Div(    
            tb.tab_3
        )
    elif tab == 'tab-4':
        return html.Div(
            tb.tab_4
        )
    elif tab == 'tab-5':
        return html.Div(
            tb.tab_5
        )

@app.callback(
 Output('time_series_one', 'figure'),
 Input('submit_button_state_one', 'n_clicks'),
 [
    ##For tab_1
    State('national_dropdown', 'value'),
    State('national_switches_input', 'value'),
    State('national_datepicker', 'start_date'),
    State('national_datepicker', 'end_date')
           
])
def update_figure(_, national_dropdown,national_switches_input, start_date, end_date):
    dff = sv.df ##Creates a copy of the dataframe
    [national_dropdown if national_dropdown != None else 'Casos totales']
    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date), national_dropdown]
    n_switches = sv.np.sum(national_switches_input)
    fig = sv.px.line(dff).update_layout(title= "National cases",
                      yaxis_title='Number of National cases',
                      xaxis_title='Date')
    if n_switches != 0:
        if n_switches==1:
            dff = dff/(sv.N/1000)
            fig = sv.px.line(dff)
            fig.update_layout(title= "National cases",
                      yaxis_title='Number of National cases per 1000 inhabitants',
                      xaxis_title='Date')
            return fig
        elif n_switches==2:
            dff = sv.np.log10(dff)
            fig = sv.px.line(dff)
            fig.update_layout(title= "National cases",
                      yaxis_title='Number of National cases (in log10 scale)',
                      xaxis_title='Date')
            return fig
        elif n_switches==3:
            dff = sv.np.log10(dff/(sv.N/1000))
            fig = sv.px.line(dff)
            fig.update_layout(title= "National cases",
                      yaxis_title='Number of National cases per 1000 inhabitants (in log10 scale)',
                      xaxis_title='Date')
            return fig
    else: return fig 

@app.callback(
    Output('time_series_two', 'figure'),
    Input('submit_button_state_two', 'n_clicks'),
    [# For tab_2
            State('regional_dropdown', 'value'),
            State('regional_cases', 'value'),
            State('regional_switches_input', 'value'),
            State('regional_datepicker', 'start_date'),
            State('regional_datepicker', 'end_date')
    ])

def regional(_,regional_dropdown,regional_cases,regional_switches_input,start_date,end_date):
    if (regional_cases == 'active'):
        dff = sv.df_region_current
    elif regional_cases == 'total':
        dff = sv.df_region_current.cumsum()
    elif regional_cases == 'deaths':
        dff = sv.df_deaths_current
    elif regional_cases == 'uci':
        dff = sv.df_uci_current   
    elif regional_cases == 'pcr':
        dff = sv.df_pcr_current

    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date),]
    dff = dff.filter(regional_dropdown, axis=1)
    fig = sv.px.line(dff
            ).update_layout(title= "Regional cases",
                      yaxis_title='Number of cases by region',
                      xaxis_title='Date')
    n_switches = sv.np.sum(regional_switches_input)
    if n_switches != 0:
        if n_switches==1:
            dff = dff/1000
            fig = sv.px.line(dff
                        ).update_layout(title= "Regional cases",
                      yaxis_title='Number of cases by region per 1000 inhabitants',
                      xaxis_title='Date')
            return fig
        elif n_switches==2:
            dff = sv.np.log10(dff)
            fig = sv.px.line(dff).update_layout(title= "Regional cases",
                      yaxis_title='Number of cases by region (in log10 scale)',
                      xaxis_title='Date')
                        
            return fig
        elif n_switches==3:
            dff = sv.np.log10(dff/1000)
            fig = sv.px.line(dff
                        ).update_layout(title= "Regional cases",
                      yaxis_title='Number of cases by region per 1000 inhabitants (in log10 scale)',
                      xaxis_title='Date')
            return fig
    else: return fig



@app.callback(
    Output('time_series_three', 'figure'),
    Input('submit_button_state_three', 'n_clicks'),
    [
            ##For tab_3
            State('seird_dropdown', 'value'),
            State('seird_datepicker', 'start_date'),
            State('seird_datepicker', 'end_date')
    ])
    
def plotrealseird(_, seird_dropdown,start_date,end_date):
    dff = sv.df_seird
    [seird_dropdown if seird_dropdown != None else ['Susceptible','Exposed','Infectious','Recovered','Deaths']]
    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date),seird_dropdown]
    fig = sv.px.line(dff
            ).update_layout(title='SEIRD model real data',
                      yaxis_title='SEIRD cases',
                      xaxis_title='Date')
    return fig

@app.callback(
    Output('time_series_four', 'figure'),
    Input('submit_button_state_four', 'n_clicks'),
    [
            ##For tab_4
            State('seirdmo_daypicker', 'date'),
            State('seirdmo_initial_cases', 'value'),
            State('seirdmo_population', 'value'),
            State('seirdmo_icu_beds', 'value'),
            State('seirdmo_p_I_to_C', 'value'),
            State('seirdmo_p_C_to_D', 'value'),
            State('seirdmo_r0_slider', 'value')
    ])

def plotseirdgo(_, date, seirdmo_initial_cases,seirdmo_population,seirdmo_icu_beds,seirdmo_p_I_to_C,seirdmo_p_C_to_D,seirdmo_r0_slider):
    fig = sv.go.Figure()
    fig.add_trace(sv.go.Line(name="Susceptible", x=sv.t, y=sv.S, line_color="dark blue"))
    fig.add_trace(sv.go.Line(name="Exposed", x=sv.t, y=sv.E, line_color="gold"))
    fig.add_trace(sv.go.Line(name="Infectious", x=sv.t, y=sv.I, line_color="red"))
    fig.add_trace(sv.go.Line(name="Recovered", x=sv.t, y=sv.R, line_color="green"))
    fig.add_trace(sv.go.Line(name="Deaths", x=sv.t, y=sv.D, line_color="black"))
    fig.update_layout(title='SEIRD model',
                      yaxis_title='SEIRD cases',
                      xaxis_title='Date')
    return fig

server = app.server
app.config.suppress_callback_exceptions = True



if __name__ == '__main__':
    app.run_server(debug=True)

