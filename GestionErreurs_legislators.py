# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 00:08:00 2018

Gestion des erreurs section

@author: jacques
"""

# library
import pandas as pd

# init variables
inputData = r'D:\udemy\Python Basics A-Z\data\legislators.csv'
outputData = r'D:\udemy\Python Basics A-Z\data\output_legislators.csv'
gender_nan = 'M'
party_nan = 'No party'

# read input data
legislator = pd.read_csv(inputData, sep=',')

# extract gender data as a list
gender = list(legislator.loc[:,'gender'].values)
# extract party data as a list
party = list(legislator.loc[:,'party'])
# extract borthday data as a list
birthday = list(legislator.loc[:,'birthday'].values)

# function to change nan
def change_nan(input_list,changed_nan):
    # loop to change NaN for No party
    for x in range(len(input_list)):
        # find nan value
        if pd.isnull(input_list[x]):
            input_list[x] = changed_nan
    return input_list

# changed nan for defined values        
gender = change_nan(gender, gender_nan)
party = change_nan(gender, party_nan)

# check gender contains only M and F
print(set(gender))

# get birth year
birth_year = []
for iBirthday in birthday:
    if pd.isnull(iBirthday):
        birth_year.append(float('nan'))
    else:
        birth_year.append(iBirthday.split('-')[0])

# convert birth year 
        # loop for each index of birth_year try to convert into int if error set 
        # birth year at the value of the precedent index (would not work it the first value is nan)
for x in range(len(birth_year)):
    try:
        birth_year[x] = int(birth_year[x])
    except:
        birth_year[x] = birth_year[x-1]

# set new birth year into legislator
legislator.loc[:,'birthday'] = birth_year
legislator.rename(columns={'birthday':'birth_year'}, inplace = True)
# print results
print(legislator.loc[:,'birth_year'])
# save results
legislator.to_csv(outputData)

'''                     test set/add/remove and list function             
# set
animals = ['chat', 'chat', 'chien', 'tigre', 'chien', 'chien']
animals.append('tortue') 
print(animals)
unique_animals = set(animals)
print(unique_animals)

# add
unique_animals.add('tortue') 
print(unique_animals)

# remove
unique_animals.remove('chat')
print(unique_animals)

# list
unique_animals = list(unique_animals)
print(unique_animals) 

# try / except
try: 
    int('') # ---> generate error in purpose
except Exception as exc:
    print(type(exc)) # ---> print error type 
    print(str(exc))  # ---> print error message with str()
'''


