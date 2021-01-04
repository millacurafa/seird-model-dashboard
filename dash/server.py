# Imports libraries

import pandas as pd
import numpy  as np
import plotly.graph_objects as go
from plotly.graph_objs.scatter.marker import Line
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
                   
px.imshow(correlations)

#Ploting Symptomatic cases

px.line(df['Casos nuevos con sintomas'],
        y= 'Casos nuevos con sintomas',
        title= "Asymptomatic cases",
        labels= dict({'Casos nuevos con sintomas':'Number of Symptomatic cases',
                     'Fecha':'Date'})
        )
#Ploting Asymptomatic cases
px.line(df['Casos nuevos sin sintomas'],
        y= 'Casos nuevos sin sintomas',
        title= "Asymptomatic cases",
        labels= dict({'Casos nuevos sin sintomas':'Number of Asymptomatic cases',
                     'Fecha':'Date'})
        )

#Ploting Total new cases

px.line(df['Casos nuevos totales'],
        y= 'Casos nuevos totales',
        title= "Daily cases",
        labels= {'Casos nuevos totales':'Number of cases',
                     'Fecha':'Date'}
        )
#Ploting Total Chilean cases

px.line(df['Casos totales'],
        y= 'Casos totales',
        title= "Total Chilean cases",
        labels= {'Fecha':'Date'}
        ).update_layout(
                    yaxis_title='Number of cases')

# Total cases in logarithmic scales

px.line(df['Casos totales'],
        y= 'Casos totales',
        title= "Total Chilean cases in logarithmic scale",
        labels= dict({'Casos totales':'Log10(Number of cases)',
                     'Fecha':'Date'}),
        log_y = True
        )    
# Adds PCR test data 
pcr_cases = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv')
pcr_cases = pcr_cases.rename(columns={'Region':'Fecha'})
pcr_cases = pcr_cases.drop([0,1])
pcr_cases = pcr_cases.set_index('Fecha')

# Plots PCR cases
px.line(pcr_cases,
        title= "PCR test per region",
        labels= {'Fecha':'Date'}
        ).update_layout(
                    yaxis_title='Number of PCR test')

# Considering the total chilean population

N = 18300000 #Chilean population; Source: World Bank

# Compartmentalisation

## Infectious cases
infectious = df[['Casos activos']].fillna(np.mean([13490,9990])) # Chilean active cases

px.line(infectious,
        title= "Infectious people",
        labels= {'Fecha':'Date'},
        ).update_layout(
                    yaxis_title='Number of infectious cases')

## Recovered Cases 1
recovered1 = df['Casos recuperados'].dropna()

px.line(recovered1,
        title="Recovered cases"
       ).update_layout(
                        yaxis_title='Number of recovered cases',
                        xaxis_title='Date'
                       )
# Recovered Cases 2
recovered2 = df['Casos confirmados recuperados'].dropna()
#df['Casos recuperados'] # Chilean recovered cases

px.line(recovered2,
        title="Recovered cases"
       ).update_layout(
                        yaxis_title='Number of recovered cases',
                        xaxis_title='Date'
                       )
#Looking for recovered data from 1st to 20th June
recovered3 = df.filter(like = '2020-06-', axis=0)['Casos recuperados por FD']

recovered3 = recovered3.drop(['2020-06-01',
                             '2020-06-21',
                             '2020-06-22',
                             '2020-06-23',
                             '2020-06-24',
                             '2020-06-25',
                             '2020-06-26',
                             '2020-06-27',
                             '2020-06-28',
                             '2020-06-29',
                             '2020-06-30'])

px.line(recovered3,
        title="Recovered cases"
       ).update_layout(
                        yaxis_title='Number of recovered cases',
                        xaxis_title='Date'
                       )
## Total Recovered cases

recovered4 = pd.DataFrame(pd.concat([recovered1,recovered3,recovered2]
                                    ),
                         columns=['Casos recuperados totales'])
px.line(recovered4,
        title="Total number of recovered cases"
       ).update_layout(
                        yaxis_title='Number of recovered cases',
                        xaxis_title='Date'
                       ) 

## Death cases
deaths = df[['Fallecidos']].fillna(0) #death cases

px.line(deaths,
        title="Total number of deaths"
       ).update_layout(
                        yaxis_title='Number of deaths',
                        xaxis_title='Date'
                       )  

# Exposed cases

exposed = df[['Casos nuevos totales']].dropna()

#For MA7
## exposed.rolling(7).mean()

px.line(exposed,
        title="Total number of exposed people"
       ).update_layout(
                        yaxis_title='Number of exposed people',
                        xaxis_title='Date'
                       )

# Susceptible cases
susceptible= pd.DataFrame()
susceptible['Casos susceptibles totales'] = N -exposed['Casos nuevos totales']- infectious['Casos activos'] - recovered4['Casos recuperados totales']-deaths['Fallecidos']
susceptible= pd.DataFrame(susceptible['Casos susceptibles totales'], columns=['Casos susceptibles totales'])
px.line(susceptible,
        title="Total number of susceptible people"
       ).update_layout(
                        yaxis_title='Number of susceptible people',
                        xaxis_title='Date'
                       )           

# Defines plot for model

def plotlyrealgo(S, E, I, R, D):
    
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

# Plots SEIRD real

plotlyrealgo(susceptible,
         exposed, 
         infectious, 
         recovered4, 
         deaths)    

# Defines derivatives

def deriv(y, t, N, beta, gamma, delta, alpha, rho):
    S, E, I, R, D = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    dRdt = (1 - alpha) * gamma * I
    dDdt = alpha * rho * I
    return dSdt, dEdt, dIdt, dRdt, dDdt     

# Defines variables and constants

N = 18300000 #Chilean population; Source: World Bank
deaths_model = 0 #deaths
recovered_model = 0 #recovered
infectious_model = 3 #infectious
susceptible_model = N -1 #susceptible
exposed_model = 0 # contracted the disease but are not yet infectious 
D = 10 # Infectious lasts
gamma = 1/D
R0 = 2 # the total number of people an infected person infects
beta = R0*gamma # infected person infects beta people per day
alpha = 0.05 # five percent death rate
rho = 1/14 # fourteen days from infection until death
delta = 1/7  # incubation period of seven days
S0, E0, I0, R0, D0 = susceptible_model, exposed_model, infectious_model, R0, deaths_model  #Initial conditions

##Creates time
t = np.linspace(0, 700) # Grid of time points (in days)
y0 = S0, E0, I0, R0, D0 # Initial conditions vector

# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta, alpha, rho))
S, E, I, R, D = ret.T

## Plots SIR model

def plotsir(t, S, I, R):
      fig = go.Figure()
      fig.add_trace(go.Line(name="Susceptible", x=t, y=S, line_color="dark blue"))
     # fig.add_trace(go.Line(name="Exposed", x=t, y=E, line_color="gold"))
      fig.add_trace(go.Line(name="Infectious", x=t, y=I, line_color="red"))
      fig.add_trace(go.Line(name="Recovered", x=t, y=R, line_color="green"))
    #  fig.add_trace(go.Line(name="Deaths", x=t, y=D, line_color="black"))
      fig.update_layout(title='SIR model',
                      yaxis_title='SIR cases',
                      xaxis_title='Date')
      return fig.show()

plotsir(t, S, I, R)

##Plots SEIR

def plotseir(t, S, E, I, R):
      fig = go.Figure()
      fig.add_trace(go.Line(name="Susceptible", x=t, y=S, line_color="dark blue"))
      fig.add_trace(go.Line(name="Exposed", x=t, y=E, line_color="gold"))
      fig.add_trace(go.Line(name="Infectious", x=t, y=I, line_color="red"))
      fig.add_trace(go.Line(name="Recovered", x=t, y=R, line_color="green"))
    #  fig.add_trace(go.Line(name="Deaths", x=t, y=D, line_color="black"))
      fig.update_layout(title='SEIR model',
                      yaxis_title='SEIR cases',
                      xaxis_title='Date')
      return fig.show()
plotseir(t, S, E, I, R)

## Plots SEIRD

def plotseird(t, S, E, I, R, D):
      fig = go.Figure()
      fig.add_trace(go.Line(name="Susceptible", x=t, y=S, line_color="dark blue"))
      fig.add_trace(go.Line(name="Exposed", x=t, y=E, line_color="gold"))
      fig.add_trace(go.Line(name="Infectious", x=t, y=I, line_color="red"))
      fig.add_trace(go.Line(name="Recovered", x=t, y=R, line_color="green"))
      fig.add_trace(go.Line(name="Deaths", x=t, y=D, line_color="black"))
      fig.update_layout(title='SEIRD model',
                      yaxis_title='SEIRD cases',
                      xaxis_title='Date')
      return fig.show()

plotseird(t, S, E, I, R, D)