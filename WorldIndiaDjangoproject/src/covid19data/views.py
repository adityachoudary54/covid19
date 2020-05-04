from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import homePageData
from datetime import datetime
#for implementation
import feedparser
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def getRss():
    newsFeed=feedparser.parse('https://www.who.int/rss-feeds/news-english.xml')
    entry=newsFeed.entries[1]
    # print(entry.keys())
    newsList=[]
    for i in newsFeed.entries:
        newsList.append([i.title,i.link,i.published])
    return newsList

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
    return df.to_html(index=False)
    
def homePage(request):
    newsList=getRss()
    # worldDataStats=worldData()
    data=homePageData.objects.filter(title='worldDataStats.html')
    if len(data)==0 :
        title='worldDataStats.html'
        contentType='HTML'
        content=worldData()
        worldDataStats=content
        homePageData.objects.create(title=title,content=content,contentType=contentType)
    else:
        data=data[0]
        # print(datetime.now(),data.modifiedDate)
        # print((datetime.now().date()-data.modifiedDate.date()).total_seconds())
        if (datetime.now().date()-data.modifiedDate.date()).total_seconds()>0:
            # print(data.pk)
            data=homePageData.objects.get(pk=data.pk)
            data.content=worldData()
            worldDataStats=data.content
            data.save()
        else:
            # print(data.pk)
            worldDataStats=data.content
    context={
        'newsList':newsList,
        'worldData':worldDataStats,
    }
    return render(request,'homePage.html',context)