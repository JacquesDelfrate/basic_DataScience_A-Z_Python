#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:47:38 2018

@author: jdelfrate
"""

import pandas as pd
import datetime as dt
import platform as plt

plt_node = plt.node()

# input data
if plt_node == 'jdelfrate':
    # guns
    inputGuns = r'D:\udemy\Python Basics A-Z\data\guns.csv'
    # census
    inputCensus = r'D:\udemy\Python Basics A-Z\data\census.csv'
else:
    # guns
    inputGuns = '/home/jdelfrate/Documents/basics_python_data/guns.csv'
    # census
    inputCensus = '/home/jdelfrate/Documents/basics_python_data/census.csv'
   
# read data csv file
guns_data = pd.read_csv(inputGuns, sep=',')
# get data frame header into
hdr_guns = list(guns_data.columns.values)

# column year
year_data = guns_data.loc[:,'year'].values
# Count how many death per year
year_count = {}
for year in year_data:
    if year in year_count:
        year_count[year] += 1
    else:
        year_count[year] = 1

# column month
month_data = guns_data.loc[:,'month'].values
# creation of object dates = dt.datetime
dates = [dt.datetime(year = year, month = month_data[x], day = 1) for x, year in enumerate(year_data)]
# Count how many death per date (year + month)
date_count = {}
for date in dates:
    if date in date_count:
        date_count[date] += 1
    else:
        date_count[date] = 1

# column sexe and race
sex_data = list(guns_data.loc[:,'sex'])
race_data = list(guns_data.loc[:,'race'])
# count death per sex and per race
sex_count = {}
race_count = {}
for sex in sex_data:
    if sex not in sex_count:
        sex_count[sex] = 0
    sex_count[sex] += 1
    
for race in race_data:
    if race not in race_count:
        race_count[race] = 0
    race_count[race] += 1

# Read census
census_data = pd.read_csv(inputCensus, sep = ',')

# dictionnary mapping
mapping = {'Asian/Pacific Islander': 15159516+674625, 'Black': 40250635,\
           'Native American/Native Alaskan': 3739506, 'Hispanic': 44618105, 'White': 197318956}
        
# ratio
ratio = {}
for race in race_count:
    ratio[race] = round(race_count[race]/mapping[race]*100000)

print(ratio)

# Filter by homidice
intents = list(guns_data.loc[:,'intent'].values)
# count homicide per race
homicide_counts = {}
for x, race in enumerate(race_data):
    if intents[x] == 'Homicide':
        if race not in homicide_counts:
            homicide_counts[race] = 0
        homicide_counts[race] += 1

print(homicide_counts)

# ratio homicide per race
homicide_ratio = {}
for race, count in homicide_counts.items():
    if race not in homicide_ratio:
        homicide_ratio[race] = 0
    homicide_ratio[race] = round(count/mapping[race]*100000)

print(homicide_ratio)            