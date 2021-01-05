import dash
from dash.dependencies import Input, Output, State
from tabs import *
#imports backend
import server as sv

## Uses bootstrap stylesheet
external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

##Creates layout

app.layout = html.Div([
    html.H1("Covid19 Analysis 🇨🇱", style={'text-align': 'left'}),
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
            tab_1
        )
    elif tab == 'tab-2':
        return html.Div(
            tab_2
        )
    elif tab == 'tab-3':
        return html.Div(    
            tab_3
        )
    elif tab == 'tab-4':
        return html.Div(
            tab_4
        )
    elif tab == 'tab-5':
        return html.Div(
            tab_5
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
    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date)]
    fig = sv.px.line(dff,
            y= dff[national_dropdown],
            title= "National cases",
            labels= dict({'Casos totales':'Number of National cases',
                        'Fecha':'Date'})
            )
    
    n_switches = len(national_switches_input)
    if n_switches != 0:
        if n_switches==1:
            dff = dff/1000
            return fig
        elif n_switches==2:
            dff = sv.np.log10(dff)
            return fig
        elif n_switches==3:
            dff = sv.np.log10(dff/1000)
            return fig
    else: return fig.show()

@app.callback(
    Output('time_series_two', 'figure'),
    Input('submit_button_state_two', 'n_clicks'),
    [##For tab_2
            State('regional_dropdown', 'value'),
            State('regional_cases', 'value'),
            State('regional_switches_input', 'value'),
            State('regional_datepicker', 'start_date'),
            State('regional_datepicker', 'end_date')
    ])

def random(_,regional_dropdown,regional_cases,regional_switches_input,start_date,end_date):
    if (regional_cases == 'total') or (regional_cases == 'active'):
        dff = sv.df_region_current
    elif regional_cases == 'deaths':
        dff = sv.df_deaths_current
    elif regional_cases == 'uci':
        dff = sv.df_uci_current   
    elif regional_cases == 'pcr':
        dff = sv.df_pcr_current

    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date)]
    fig = sv.px.line(dff,
            y= dff[regional_dropdown],
            title= "Regional cases",
            labels= dict({'Casos nuevos con sintomas':'Number of cases by region',
                        'Fecha':'Date'})
            )
    return fig.show()

@app.callback(
    Output('time_series_three', 'figure'),
    Input('submit_button_state_three', 'n_clicks'),
    [
            ##For tab_3
            State('seird_dropdown', 'value'),
            State('seird_datepicker', 'start_date'),
            State('seird_datepicker', 'end_date')
    ])

def random1(_,seird_dropdown,start_date,end_date):
    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date)]    
    fig = go.Figure()
    fig.add_trace(go.Line(name="Susceptible", x=S.index, y=np.log10(S.iloc[:, 0]), line_color="dark blue"))
    fig.add_trace(go.Line(name="Exposed", x=E.index, y=np.log10(E.iloc[:, 0]), line_color="gold"))
    fig.add_trace(go.Line(name="Infectious", x=I.index, y=np.log10(I.iloc[:, 0]), line_color="red"))
    fig.add_trace(go.Line(name="Recovered", x=R.index, y=np.log10(R.iloc[:, 0]), line_color="green"))
    fig.add_trace(go.Line(name="Deaths", x=D.index, y=np.log10(D.iloc[:, 0]), line_color="black"))
    fig.update_layout(title='SEIRD model real data',
                      yaxis_title='SEIRD cases',
                      xaxis_title='Date')
    return fig.show()

@app.callback(
    Output('time_series_four', 'figure'),
    Input('submit_button_state_four', 'n_clicks'),
    [
            ##For tab_4
            State('seirdmo_daypicker', 'start_date'),
            State('seirdmo_daypicker', 'end_date'),
            State('seirdmo_initial_cases', 'value'),
            State('seirdmo_population', 'value'),
            State('seirdmo_icu_beds', 'value'),
            State('seirdmo_p_I_to_C', 'value'),
            State('seirdmo_p_C_to_D', 'value'),
            State('seirdmo_r0_slider', 'value')
    ])

def random2():
    dff = dff.loc[(dff.index >= start_date) & (dff.index <= end_date)]    
    fig = go.Figure()
    fig.add_trace(go.Line(name="Susceptible", x=S.index, y=np.log10(S.iloc[:, 0]), line_color="dark blue"))
    fig.add_trace(go.Line(name="Exposed", x=E.index, y=np.log10(E.iloc[:, 0]), line_color="gold"))
    fig.add_trace(go.Line(name="Infectious", x=I.index, y=np.log10(I.iloc[:, 0]), line_color="red"))
    fig.add_trace(go.Line(name="Recovered", x=R.index, y=np.log10(R.iloc[:, 0]), line_color="green"))
    fig.add_trace(go.Line(name="Deaths", x=D.index, y=np.log10(D.iloc[:, 0]), line_color="black"))
    fig.update_layout(title='SEIRD model real data',
                      yaxis_title='SEIRD cases',
                      xaxis_title='Date')
    return fig.show()

server = app.server
app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)