import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import wget
from bs4 import BeautifulSoup
import urllib.request

url = "https://pomber.github.io/covid19/timeseries.json"

def download():
    reqPath=os.path.abspath("./worldStatistics/trendsData")
    if "timeseries.json" not in os.listdir(reqPath):
        wget.download(url, os.path.join(reqPath,'timeseries.json'))

def printData():
    timeSeriesDf=pd.read_json('./worldStatistics/trendsData/timeseries.json')
    print(timeSeriesDf.head())

download()
timeSeriesDf=pd.read_json('./worldStatistics/trendsData/timeseries.json')

def cleanedData(timeSeriesDf):
    data={}
    for x,y in timeSeriesDf.items(): 
        dataCountry=pd.DataFrame.from_dict(y[0],orient='index')
        for index,item in enumerate(y[1:]):
            s2=pd.DataFrame.from_dict(item,orient='index')
            dataCountry=pd.concat([dataCountry,s2],axis=1)
        dataCountry=dataCountry.T
        data[x]=dataCountry
    return data

data=cleanedData(timeSeriesDf)
def countryList():
    return list(data.keys()) 

def countryPlotLy(countryName,casetype):
    temp=os.path.abspath("./worldStatistics/trendsData")
    path=os.path.join(temp,'{} {} trends.html'.format(countryName,casetype))
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName][casetype],
                        mode='lines+markers',
                        name='{} cases'.format(casetype)))
    # fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['deaths'],
    #                     mode='lines',
    #                     name='Deaths'))
    # fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['recovered'],
    #                     mode='lines', name='Recovered'))
    # fig.add_trace(go.Scatter(x=data[countryName]['date'], y=data[countryName]['confirmed']-data[countryName]['deaths']-data[countryName]['recovered'],
    #                     mode='lines+markers', name='Actual cases remaining'))
    fig.update_layout(      
        height=600,
        width=800,
        title='{} covid19 {} cases statistics'.format(countryName,casetype),
        xaxis_title="Date",
        yaxis_title="Number of cases",
        font=dict(
                family="Arial",
                size=12,
                color='black'
            ),
    )
    fig.write_html(path)
    f=open(path, "r")
    contents=f.read()
    soup=BeautifulSoup(contents,'html.parser')
    div=str(soup.find('div'))
    return div

# countryPlotLy('India',data)