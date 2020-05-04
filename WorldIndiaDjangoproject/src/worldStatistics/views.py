from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from datetime import datetime
#for implementation
import feedparser
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
from . import trendsScript
from . import topNcountries
import json
# Create your views here.
def generateTrendsData(countryList,typeList):
    data={}
    for country in countryList:
        dataCases={}
        for caseType in typeList:
            dataCases[caseType]=trendsScript.countryPlotLy(country,caseType)
        data[country]=dataCases
    with open('./worldStatistics/trendsData/data.json', 'w') as fp:
        json.dump(data, fp)
    return data

def trends(request):
    countryList=trendsScript.countryList()
    # data=generateTrendsData(countryList,['confirmed','recovered','deaths'])
    if request.POST:
        countryName=request.POST.get('countryName')
        caseType=request.POST.get('caseType')
        data=trendsScript.countryPlotLy(countryName,caseType)
    else:
        data="Click on the options to generate graph"
    context={
        'countryList':countryList,
        'data':data
    }
    return render(request,'worldStatistics/trends.html',context)

def top5(request):
    countList=range(1,topNcountries.countCountries()+1)
    if request.POST:
        count=request.POST.get('count')
        caseType=request.POST.get('caseType')
        data=topNcountries.histTopNcountries(int(count),caseType)
    else:
        data="Click on the options to generate graph"
    context={
        'countList':countList,
        'data':data
    }
    return render(request,'worldStatistics/topNcountries.html',context)
