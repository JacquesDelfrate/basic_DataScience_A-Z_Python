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
    inputData = r'D:\udemy\Python Basics A-Z\data\guns.csv'
else:
    inputData = '/home/jdelfrate/Documents/basics_python_data/guns.csv'
    
# read data csv file
guns_data = pd.read_csv(inputData, sep=',')
# get data frame header into
hdr = list(guns_data.columns.values)

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