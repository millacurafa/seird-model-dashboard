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
@app.callback(
 Output('time-series', 'figure'),
 Input('submit_button_state', 'n_clicks'),
 [
            ##For tab_1
            State('national_dropdown', 'value'),
            State('national_switches_input', 'value'),
            State('national_datepicker', 'date'),
            ##For tab_2
            State('regional_dropdown', 'value'),
            State('regional_cases', 'value'),
            State('regional_switches_input', 'value'),
            State('regional_datepicker', 'date'),
            ##For tab_3
            State('seird-dropdown', 'value'),
            State('seird_datepicker', 'date'),
            ##For tab_4
            State('seirdmo_daypicker', 'date'),
            State('seirdmo_initial_cases', 'value'),
            State('seirdmo_population', 'value'),
            State('seirdmo_icu_beds', 'value'),
            State('seirdmo_p_I_to_C', 'value'),
            State('seirdmo_p_C_to_D', 'value'),
            State('seirdmo_r0_slider', 'value')
            
]

)
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            tab_1
        ])
    elif tab == 'tab-2':
        return html.Div([
            tab_2
        ])
    elif tab == 'tab-3':
        return html.Div([    
            tab_3
        ])
    elif tab == 'tab-4':
        return html.Div([
            tab_4
        ])
    elif tab == 'tab-5':
        return html.Div([
            tab_5
        ])


#def render_main_content(national_dropdown, national_switches_input, date_picker_range):
#      fig = sv.go.Figure()
#      fig.add_trace(sv.go.Line(name="Total cases", x=date_picker_range, y=sv.df[national_switches_input], line_color="dark blue"))
#      fig.add_trace(sv.go.Line(name="Active cases", x=date_picker_range, y=sv.df[national_switches_input], line_color="gold"))
#      fig.add_trace(sv.go.Line(name="Deaths", x=date_picker_range, y=sv.df[national_switches_input], line_color="red"))
#      fig.add_trace(sv.go.Line(name="Recovered", x=date_picker_range, y=sv.df[national_switches_input], line_color="green"))
#      fig.add_trace(sv.go.Line(name="PCR tests", x=date_picker_range, y=sv.df[national_switches_input], line_color="purple"))
    #  fig.add_trace(go.Line(name="Deaths", x=t, y=D, line_color="black"))
#      fig.update_layout(title='National cases',
#                      yaxis_title='Number of cases',
#                      xaxis_title='Date')
#      return fig.show()

##server = app.server
##app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
    app.run_server(debug=True)