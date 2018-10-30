#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 08:39:28 2018

@author: jdelfrate
"""

import pandas as pd
import platform as plt
import re
import datetime as dt


plt_node = plt.node()

if plt_node == 'megawatt':
    inputData = '/home/jdelfrate/Documents/basics_python_data/askreddit-2015.csv'
else:
    inputData

post = pd.read_csv(inputData, sep = ',')

# Find how many time 'of Reddit' is in the title assign results to of_reddit_count
titles = list(post.loc[:,'Title'].values)
of_reddit_count = 0
for title in titles:
    if re.search('of [rR]eddit', title) is not None: # [] permet de sélectionner toutes les lettres entre les crochets ici of reddit and of Reddit
        of_reddit_count += 1

# Find how many time  [Serious] is in a title. Assign result to serious_count
# Use \ pour ignorer les charactères spéciaux
# Use | to combien regex
serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for title in titles:
    if re.search('^[\[\(][Ss]erious[\]\)]', title) is not None:
        serious_start_count +=1
    if re.search('[\[\(][Ss]erious[\]\)]$', title) is not None:
        serious_end_count += 1
    if re.search('^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$', title) is not None:
        serious_count_final += 1

# Change [serious], (serious), (Serious) by [Serious] add new title to list posts_new
posts_new = []
for title in titles:
    title = re.sub('[\[\(][Ss]erious[\)\]]', '[Serious]', title)
    posts_new.append(title)
    
# convert time into year
times = list(post.loc[:,'Time'].values)
# datetime.fromtimestamp()
new_times = [dt.datetime.fromtimestamp(time) for time in times]

# put new time into data frame
post.loc[:,'Time'] = new_times

# count number of date with may
count_may = 0
for new_time in new_times:
    if new_time.month == 5:
        count_may += 1
print(count_may)



# function that computes number of post of an input number of month
def posts_count(month):
    count_post = 0
    for new_time in new_times:
        if new_time.month == month:
            count_post += 1
    return count_post

# apply to all month
count_month = []
for i in range(12):
    count = posts_count(i+1)
    count_month.append(count)
    print(count)

# re.search(regex, string) --> correspondance entre string et le regex
if re.search('f.', 'kungfu') is not None:
    print('Trouvé')
else:
    print('Pas de correspondance')
    
# replace chaine de charactere
re.sub('yo', 'hello' , 'yo world!')

# findall()
string_years = 'On est déjà en 2017, une année de plus quand 2016 et une de moins que 2018'
year = re.findall('[1-2][0-9]{3}', string_years)
print(year)