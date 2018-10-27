# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 03:49:03 2018

Explore birth in the US since 2000
Not adaptation of the code in class with panda, and numpy to learn how to use 
those library

@author: jacques
"""

# import library
import pandas as pd
import numpy as np

''' path '''
inputData = r'D:\udemy\Python Basics A-Z\data\US-births-2000-2014.csv'

''' read data '''
data = pd.read_csv(inputData, sep=',')
time_year = 'year'

# generic function to compute birth
# can be per day, per month or per year
def calc_counts(data, time_year):
    ''' extract column month and birth '''
    time_year = list(data.loc[:,time_year].values)
    birth     = list(data.loc[:,'births'].values)
    ''' add number of birth per month '''
    birth_time = {}
    for x in range(data.shape[0]):
        selected_time = time_year[x]
        births = birth[x]
        if selected_time in birth_time:
            birth_time[selected_time] += births
        else:
            birth_time[selected_time] = births
    return birth_time

# compute number of birth per month
def month_birth(data):
    ''' extract column month and birth '''
    month = data.loc[:,'month'].values
    birth = data.loc[:,'births'].values
    ''' find unique of month and organise output matrix '''
    uniMonth = pd.unique(month)
    us_month_birth = np.zeros((uniMonth.shape[0],2))
    us_month_birth[:,0] = uniMonth
    ''' add number of birth per month '''
    i=0
    for iMonth in month:
        us_month_birth[iMonth-1,1] += birth[i]
        i+=1
    ''' convert matrix from float64 to int64 '''
    us_month_birth = us_month_birth.astype('int64')
    ''' convert to dictonnary (to folow the class)'''
    us_month_birth = dict((x[0], x[1]) for x in us_month_birth[0:])
    ''' return output '''
    return us_month_birth

# compute number of birth per day
def day_perWeek_birth(data):
    ''' extract column month and birth '''
    day = data.loc[:,'day_of_week'].values
    birth = data.loc[:,'births'].values
    ''' find unique of month and organise output matrix '''    
    uniDay = pd.unique(day)
    us_day_birth = np.zeros((uniDay.shape[0],2))
    uniDay = sorted(uniDay)
    us_day_birth[:,0] = uniDay
    ''' compute number of birth per day '''
    i=0
    for iday in day:
        us_day_birth[iday-1,1] += birth[i]
        i+=1
    ''' convert matrix into int64 '''
    us_day_birth = us_day_birth.astype('int64')
    ''' convert to dictionnary '''
    us_day_birth = dict((x[0],x[1]) for x in us_day_birth[0:])
    return us_day_birth
#us_month_birth = month_birth(data)
#print(us_month_birth)

#us_day_birth = day_perWeek_birth(data)
#print(us_day_birth)

us_year_birth = calc_counts(data, time_year)
print(us_year_birth)

      



"""df2 = pd.DataFrame(birth)
us_mont_birth = pd.concat([df1,df2], axis=1)
uniMonth = pd.unique(month)
        
        
        
dataV2 = open(inputData, 'r').read()
dataV2 = dataV2.split('\n')

print(us_mont_birth) """
