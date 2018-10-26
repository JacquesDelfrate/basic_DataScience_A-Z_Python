# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 03:49:03 2018

Explore birth in the US since 2000

@author: jacques
"""

import pandas as pd

inputData = r'D:\udemy\Python Basics A-Z\data\US-births-2000-2014.csv'

dataV1 = pd.read_csv(inputData, sep=',')
month = dataV1.iloc[:,1].values
uniMonth = pd.unique(month)
birth = dataV1.iloc[:,4].values
us_mont_birth = pd.concat([df1,df2], axis=1)

prout = {}
for iMonth in month:
    if iMonth in prout:
        prout[iMonth] += birth+birth[iMonth]
    else:
        prout[iMonth] = birth[iMonth]
        
df1 = pd.DataFrame(month)
df2 = pd.DataFrame(birth)
us_mont_birth = pd.concat([df1,df2], axis=1)

dataV2 = open(inputData, 'r').read()
dataV2 = dataV2.split('\n')

print(us_mont_birth)
