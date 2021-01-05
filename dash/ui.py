import dash
from dash.dependencies import Input, Output, State
from tabs import *
#imports backend
import server as sv


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


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
            State('national_datepicker', 'date')
           
])
#def plot():
#    sv.px.scatter(px.data.iris(), x="sepal_width", y="sepal_length"

@app.callback(
    Output('time_series_two', 'figure'),
    Input('submit_button_state_two', 'n_clicks'),
    [##For tab_2
            State('regional_dropdown', 'value'),
            State('regional_cases', 'value'),
            State('regional_switches_input', 'value'),
            State('regional_datepicker', 'date')
    ])

@app.callback(
    Output('time_series_three', 'figure'),
    Input('submit_button_state_three', 'n_clicks'),
    [
            ##For tab_3
            State('seird-dropdown', 'value'),
            State('seird_datepicker', 'date')
    ])



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

server = app.server
app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)