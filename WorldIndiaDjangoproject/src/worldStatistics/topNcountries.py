import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import wget

def worldData():
    req=urllib.request.urlopen('https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory')
    soup=BeautifulSoup(req,'html.parser')

    tb=soup.find('table',attrs={'id':'thetable'})
    gdp_table_data = tb.tbody.find_all("tr")

    data = {}
    for tr in gdp_table_data[2:len(gdp_table_data)-2]:
        # for i in tr.find_all('th'):
        # print(tr.find_all('th')[1].text)
        temp=tr.find_all('th')
        if len(temp)<=1:
            break
        a=[tr.find_all('th')[1].find('a').text]    
        for i in tr.find_all('td')[0:3]:
            l=i.text.rstrip('\n')
            
            if l=='–' or l=='—':
                a.append('Unknown')
            if l.find(',')!=-1:
                a.append(int(l.replace(',','')))
            else:
                
                if l!='–' and l!='—':
                    # print('hello',l)
                    a.append(int(l))    
        data[tr.find_all('th')[1].find('a').text]=a
    # print(data)

    df=pd.DataFrame.from_dict(data)
    df=df.T
    df.columns=['Country','Cases','Deaths','Recovered']
    return df.reset_index(drop=True)

df=worldData()
def countCountries():
    return df.shape[0]

def generateReqData(n):
    df.sort_values(by=['Cases'], inplace=True, ascending=False)
    return df.head(n=n)

def histTopNcountries(n,caseType):
    x=[caseType]
    reqData=generateReqData(n)
    fig=go.Figure()
    for i in range(n):
        y=reqData.iloc[i,1:]
        fig.add_trace(go.Histogram(histfunc="sum", y=y, x=x, name=reqData.iloc[i,0]))
    fig.update_layout(
        title="Top {} cases comparision".format(n),
        yaxis_title="Number of Cases",
        font=dict(
            family="Courier New, monospace",
            size=14,
        )
    )

    temp=os.path.abspath("./worldStatistics/trendsData")
    path=os.path.join(temp,'Top {} {} histogram.html'.format(n,caseType))

    fig.write_html(path)
    f=open(path, "r")
    contents=f.read()
    soup=BeautifulSoup(contents,'html.parser')
    div=str(soup.find('div'))
    return div