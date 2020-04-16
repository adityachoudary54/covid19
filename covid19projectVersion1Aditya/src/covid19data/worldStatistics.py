import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

import wget

url = "https://pomber.github.io/covid19/timeseries.json"

if "timeseries.json" not in os.listdir('/home/aditya/Documents/WebDev/WorldIndiaDjangoproject/src/covid19data/worldStatisticsData'):
    wget.download(url, '/home/aditya/Documents/WebDev/WorldIndiaDjangoproject/src/covid19data/worldStatisticsData/timeseries.json')

# print(os.getcwd())
timeSeriesDf=pd.read_json('./worldStatisticsData/timeseries.json')
# print(timeSeriesDf.head())
def cleanedData(timeSeriesDf):
    data={}
    for x,y in timeSeriesDf.items(): 
        dataCountry=pd.DataFrame.from_dict(y[0],orient='index')
        for index,item in enumerate(y[1:]):
            s2=pd.DataFrame.from_dict(item,orient='index')
            dataCountry=pd.concat([dataCountry,s2],axis=1)
        dataCountry=dataCountry.T
        # print(dataCountry.keys(),dataCountry['date'],dataCountry['confirmed'],dataCountry.shape)
        data[x]=dataCountry
    return data

data=cleanedData(timeSeriesDf)

def countryPlotLy(countryName,data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['confirmed'],
                        mode='lines',
                        name='Confirmed cases'))
    fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['deaths'],
                        mode='lines',
                        name='Deaths'))
    fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['recovered'],
                        mode='lines', name='Recovered'))
    fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['confirmed']-data[countryName]['deaths']-data[countryName]['recovered'],
                        mode='lines+markers', name='Actual cases remaining'))
    fig.update_layout(      
        height=500,
        width=800,
        title='{} covid19 statistics'.format(countryName),
        xaxis_title="Date",
        yaxis_title="Number of cases",
        font=dict(
                family="Arial",
                size=12,
                color='black'
            ),
    )
#   if '{}CoronaStatistics.html'.format(countryName) not in os.listdir('/home/aditya/Documents/WebDev/WorldIndiaDjangoproject/src/covid19data/worldStatisticsData'):
    fig.write_html('/home/aditya/Documents/WebDev/WorldIndiaDjangoproject/src/covid19data/worldStatisticsData/{}CoronaStatistics.html'.format(countryName))
#   fig.show()

countryPlotLy('India',data)