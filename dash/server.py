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
                   
correlate = px.imshow(correlations)

demoplot = figure= px.scatter(px.data.iris(), x="sepal_width", y="sepal_length")
