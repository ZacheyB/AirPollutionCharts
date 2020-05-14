from django.shortcuts import render
from django.http import HttpResponse

import json
import os

import numpy as np
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def los_angeles(request):
    if os.path.exists('homepage/graphdata/echart.json'):
        os.remove('homepage/graphdata/echart.json')

    df = pd.read_csv('http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States_of_America/California/Los_Angeles.txt', sep='\t', skiprows=10)
    df.columns = ['year', 'month', 'day', 'hour', 'pm2_5', 'pm10_mask', 'retro']
    export_df = pd.DataFrame()
    export_df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    export_df['pm2_5'] = df['pm2_5']
    export_df = export_df.set_index('date_time')
    averages = export_df.resample('M').mean()
    march_2018 = averages.loc['2018-03-31']['pm2_5']
    april_2018 = averages.loc['2018-04-30']['pm2_5']
    may_2018 = averages.loc['2018-05-31']['pm2_5']
    march_2019 = averages.loc['2019-03-31']['pm2_5']
    april_2019 = averages.loc['2019-04-30']['pm2_5']
    may_2019 = averages.loc['2019-05-31']['pm2_5']
    march_2020 = averages.loc['2020-03-31']['pm2_5']
    april_2020 = averages.loc['2020-04-30']['pm2_5']
    may_2020 = averages.loc['2020-05-31']['pm2_5']

    export_df = pd.DataFrame()
    export_df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    export_df['date_time'] = export_df['date_time'].dt.strftime('%Y-%m-%d-%r')
    export_df['pm2_5'] = df['pm2_5'] 
    vals = export_df.values
    vals = vals.tolist()

    with open('homepage/graphdata/echart.json', 'w') as f:
        f.write(json.dumps(vals))

    context = {
        'city_name': 'Los Angeles',
        'march_2018': march_2018,
        'april_2018': april_2018,
        'may_2018': may_2018,
        'march_2019': march_2019,
        'april_2019': april_2019,
        'may_2019': may_2019,
        'march_2020': march_2020,
        'april_2020': april_2020,
        'may_2020': may_2020,
    }

    return render(request, 'homepage/index.html', context = context)

def newyork(request):
    if os.path.exists('homepage/graphdata/echart.json'):
        os.remove('homepage/graphdata/echart.json')

    df = pd.read_csv('http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States_of_America/New_York/New_York_City.txt', sep='\t', skiprows=10)
    df.columns = ['year', 'month', 'day', 'hour', 'pm2_5', 'pm10_mask', 'retro']
    export_df = pd.DataFrame()
    export_df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    export_df['pm2_5'] = df['pm2_5']
    export_df = export_df.set_index('date_time')
    averages = export_df.resample('M').mean()
    #march_2018 = averages.loc['2018-03-31']['pm2_5']
    #april_2018 = averages.loc['2018-04-30']['pm2_5']
    #may_2018 = averages.loc['2018-05-31']['pm2_5']
    #march_2019 = averages.loc['2019-03-31']['pm2_5']
    #april_2019 = averages.loc['2019-04-30']['pm2_5']
    #may_2019 = averages.loc['2019-05-31']['pm2_5']
    #march_2020 = averages.loc['2020-03-31']['pm2_5']
    #april_2020 = averages.loc['2020-04-30']['pm2_5']
    #may_2020 = averages.loc['2020-05-31']['pm2_5']

    export_df = pd.DataFrame()
    export_df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    export_df['date_time'] = export_df['date_time'].dt.strftime('%Y-%m-%d-%r')
    export_df['pm2_5'] = df['pm2_5'] 
    vals = export_df.values
    vals = vals.tolist()

    with open('homepage/graphdata/echart.json', 'w') as f:
        f.write(json.dumps(vals))

    context = {
        'city_name': 'New York',
        'march_2018': 'Only data until 2016 is listed.',
        'april_2018': 0,
        'may_2018': 0,
        'march_2019': 0,
        'april_2019': 0,
        'may_2019': 0,
        'march_2020': 0,
        'april_2020': 0,
        'may_2020': 0,
    }

    return render(request, 'homepage/index.html', context = context)

def san_diego(request):
    if os.path.exists('homepage/graphdata/echart.json'):
        os.remove('homepage/graphdata/echart.json')

    df = pd.read_csv('http://berkeleyearth.lbl.gov/air-quality/maps/cities/United_States_of_America/California/San_Diego.txt', sep='\t', skiprows=10)
    df.columns = ['year', 'month', 'day', 'hour', 'pm2_5', 'pm10_mask', 'retro']
    export_df = pd.DataFrame()
    export_df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    export_df['pm2_5'] = df['pm2_5']
    export_df = export_df.set_index('date_time')
    averages = export_df.resample('M').mean()
    march_2018 = averages.loc['2018-03-31']['pm2_5']
    april_2018 = averages.loc['2018-04-30']['pm2_5']
    may_2018 = averages.loc['2018-05-31']['pm2_5']
    march_2019 = averages.loc['2019-03-31']['pm2_5']
    april_2019 = averages.loc['2019-04-30']['pm2_5']
    may_2019 = averages.loc['2019-05-31']['pm2_5']
    march_2020 = averages.loc['2020-03-31']['pm2_5']
    april_2020 = averages.loc['2020-04-30']['pm2_5']
    may_2020 = averages.loc['2020-05-31']['pm2_5']

    export_df = pd.DataFrame()
    export_df['date_time'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    export_df['date_time'] = export_df['date_time'].dt.strftime('%Y-%m-%d-%r')
    export_df['pm2_5'] = df['pm2_5'] 
    vals = export_df.values
    vals = vals.tolist()

    with open('homepage/graphdata/echart.json', 'w') as f:
        f.write(json.dumps(vals))

    context = {
        'city_name': 'San Diego',
        'march_2018': march_2018,
        'april_2018': april_2018,
        'may_2018': may_2018,
        'march_2019': march_2019,
        'april_2019': april_2019,
        'may_2019': may_2019,
        'march_2020': march_2020,
        'april_2020': april_2020,
        'may_2020': may_2020,
    }

    return render(request, 'homepage/index.html', context = context)