# Imports libraries

import pandas as pd
import numpy  as np
import plotly.graph_objects as go
from plotly.graph_objs.scatter.marker import Line
import plotly.express as px
from scipy.integrate import odeint

##Imports regional data
df_city_current = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto25/CasosActualesPorComuna_std.csv")

# regional daily active cases

df_region_current = df_city_current[df_city_current["Comuna"] == "Total"]

df_region_current_bypop = df_city_current[df_city_current["Comuna"] == "Total"]
df_region_current_bypop['bypop'] = df_region_current.loc[0:,"Casos actuales"]/(df_region_current.loc[0:,"Poblacion"]/1000)
df_region_current_bypop = df_region_current_bypop[["Region", "Fecha", "bypop", 'Casos actuales']].pivot(index='Fecha', columns='Region', values=['bypop', 'Casos actuales'])
df_region_current_bypop

df_region_current = df_region_current[["Region", "Fecha", "Casos actuales"]].pivot(index='Fecha', columns='Region', values='Casos actuales')

###Deaths

df_city_deaths = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto38/CasosFallecidosPorComuna_std.csv")
df_deaths_region = df_city_deaths[df_city_deaths['Comuna']=='Total'].groupby(['Region','Fecha'])[['Casos fallecidos']].sum()   
df_deaths_current = df_deaths_region.reset_index().pivot(index='Fecha', columns='Region', values='Casos fallecidos')

df_city_deaths['bypop']= df_city_deaths[df_city_deaths['Comuna']=='Total']['Casos fallecidos']/(df_city_deaths[df_city_deaths['Comuna']=='Total']['Poblacion']/1000)
df_deaths_region_bypop  = df_city_deaths[df_city_deaths['Comuna']=='Total'].groupby(['Region','Fecha'])[['Casos fallecidos','bypop']].sum()    
df_deaths_current_bypop  = df_deaths_region_bypop.reset_index().pivot(index='Fecha', columns='Region', values=['bypop', 'Casos fallecidos'])

###Number of PCR exams

df_pcr_region = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_std.csv")

df_pcr_current = df_pcr_region[['Region', 'fecha', 'numero']].pivot(index='fecha', columns='Region', values='numero')


#Critical patients
df_uci_region = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto8/UCI_std.csv")

df_uci_current = df_uci_region[['Region', 'fecha', 'numero']].pivot(index='fecha', columns='Region', values='numero')

#Imports national data

df = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales_T.csv',
                error_bad_lines=False
                 )

df= df.set_index('Fecha')



#Checking for data correlations

#correlations = df[['Casos totales',
#                   'Casos recuperados',
#                   'Fallecidos',
#                   'Casos activos',
#                   'Casos nuevos totales',
#                  'Casos nuevos con sintomas',
#                  'Casos nuevos sin sintomas']].corr()
                   
#px.imshow(correlations)

#Ploting Symptomatic cases

#px.line(df['Casos nuevos con sintomas'],
#        y= 'Casos nuevos con sintomas',
#        title= "Asymptomatic cases",
#        labels= dict({'Casos nuevos con sintomas':'Number of Symptomatic cases',
#                     'Fecha':'Date'})
#        )
#Ploting Asymptomatic cases
#px.line(df['Casos nuevos sin sintomas'],
#        y= 'Casos nuevos sin sintomas',
#        title= "Asymptomatic cases",
#        labels= dict({'Casos nuevos sin sintomas':'Number of Asymptomatic cases',
#                     'Fecha':'Date'})
#        )

#Ploting Total new cases

#px.line(df['Casos nuevos totales'],
#        y= 'Casos nuevos totales',
#        title= "Daily cases",
#        labels= {'Casos nuevos totales':'Number of cases',
#                     'Fecha':'Date'}
#        )
#Ploting Total Chilean cases

#px.line(df['Casos totales'],
#        y= 'Casos totales',
#        title= "Total Chilean cases",
#        labels= {'Fecha':'Date'}
#        ).update_layout(
#                    yaxis_title='Number of cases')

# Total cases in logarithmic scales

#px.line(df['Casos totales'],
#        y= 'Casos totales',
#        title= "Total Chilean cases in logarithmic scale",
#        labels= dict({'Casos totales':'Log10(Number of cases)',
#                     'Fecha':'Date'}),
#        log_y = True
#        )    
# Adds PCR test data 
pcr_cases = pd.read_csv('https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv')
pcr_cases = pcr_cases.rename(columns={'Region':'Fecha'})
pcr_cases = pcr_cases.drop([0,1])
pcr_cases = pcr_cases.set_index('Fecha')

# Plots PCR cases
#px.line(pcr_cases,
#        title= "PCR test per region",
#       labels= {'Fecha':'Date'}
#        ).update_layout(
#                    yaxis_title='Number of PCR test')

# Considering the total chilean population

N = 18300000 #Chilean population; Source: World Bank

# Compartmentalisation

## Infectious cases
infectious = df[['Casos activos']].fillna(np.mean([13490,9990])) # Chilean active cases

recovered1 = df['Casos recuperados'].dropna()

# Recovered Cases 2
recovered2 = df['Casos confirmados recuperados'].dropna()

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

## Total Recovered cases

recovered4 = pd.DataFrame(pd.concat([recovered1,recovered3,recovered2]
                                    ),
                         columns=['Casos recuperados totales'])


#adding recovered variable into national 

df['recovered'] = recovered4['Casos recuperados totales']
 

## Death cases
deaths = df[['Fallecidos']].fillna(0) #death cases

# Exposed cases

exposed = df[['Casos nuevos totales']].dropna()

#For MA7
## exposed.rolling(7).mean()


# Susceptible cases
susceptible= pd.DataFrame()
susceptible['Casos susceptibles totales'] = N -exposed['Casos nuevos totales']- infectious['Casos activos'] - recovered4['Casos recuperados totales']-deaths['Fallecidos']
susceptible= pd.DataFrame(susceptible['Casos susceptibles totales'], columns=['Casos susceptibles totales'])

# Concats SEIRD df

df_seird = susceptible.join([exposed, infectious, recovered4, deaths])
df_seird = df_seird.rename(columns={"Casos susceptibles totales": "Susceptible", 
                                    "Casos nuevos totales": "Exposed",
                                    "Casos activos":"Infectious",
                                    "Casos recuperados totales":"Recovered",
                                    "Fallecidos":"Dead"})


# Defines derivatives

def derivate(y, t, N, beta, gamma, delta, alpha, rho):
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
ret = odeint(derivate, y0, t, args=(N, beta, gamma, delta, alpha, rho))
S, E, I, R, D = ret.T


def plotlyseirdgo(t, S, E, I, R, D):
      fig = go.Figure()
      fig.add_trace(go.Line(name="Susceptible", x=t, y=S, line_color="dark blue"))
      fig.add_trace(go.Line(name="Exposed", x=t, y=E, line_color="gold"))
      fig.add_trace(go.Line(name="Infectious", x=t, y=I, line_color="red"))
      fig.add_trace(go.Line(name="Recovered", x=t, y=R, line_color="green"))
      fig.add_trace(go.Line(name="Deaths", x=t, y=D, line_color="black"))
      fig.update_layout(title='SEIRD model simulation',
                      yaxis_title='SEIRD cases',
                      xaxis_title='Number of days')
      return fig

# def plotlyrealgo(S, E, I, R, D):    
#     fig = go.Figure()
#     fig.add_trace(go.Line(name="Susceptible", x=S.index, y=S.iloc[:, 0], line_color="dark blue"))
#     fig.add_trace(go.Line(name="Exposed", x=E.index, y=E.iloc[:, 0], line_color="gold"))
#     fig.add_trace(go.Line(name="Infectious", x=I.index, y=I.iloc[:, 0], line_color="red"))
#     fig.add_trace(go.Line(name="Recovered", x=R.index, y=R.iloc[:, 0], line_color="green"))
#     fig.add_trace(go.Line(name="Deaths", x=D.index, y=D.iloc[:, 0], line_color="black"))
#     fig.update_layout(title='SEIRD model real data',
#                       yaxis_title='SEIRD cases',
#                       xaxis_title='Date')
#     return fig
# def plotrealgo(_, seird_dropdown,start_date,end_date):
#     S, E, I, R, D = susceptible, exposed, infectious, recovered4, deaths
#         fig = go.Figure().update_layout(title='SEIRD model real data',
#                         yaxis_title='SEIRD cases',
#                         xaxis_title='Date')    
#         for chosen in seird_dropdown:
            
#             if (chosen == 'S'):
#                 fig.add_trace(go.Line(name="Susceptible", x=S.index.loc[(S.index >= start_date) & (S.index <= end_date)], y=S.iloc[:, 0], line_color="dark blue"))
#                 return fig
#             elif (chosen == 'E'):
#                 fig.add_trace(go.Line(name="Exposed", x=E.index.loc[(E.index >= start_date) & (E.index <= end_date)], y=E.iloc[:, 0], line_color="gold"))
#                 return fig
#             elif (chosen == 'I'):
#                 fig.add_trace(go.Line(name="Infectious", x=I.index.loc[(I.index >= start_date) & (I.index <= end_date)], y=I.iloc[:, 0], line_color="red"))
#                 return fig
#             elif (chosen == 'R'):
#                 fig.add_trace(go.Line(name="Recovered", x=R.index.loc[(R.index >= start_date) & (R.index <= end_date)], y=R.iloc[:, 0], line_color="green"))
#                 return fig
#             elif (chosen == 'D'):
#                 fig.add_trace(go.Line(name="Deaths", x=D.index.loc[(D.index >= start_date) & (D.index <= end_date)], y=D.iloc[:, 0], line_color="black"))
#                 return fig
#             else: return fig