# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 01:42:31 2018

@author: jacques
"""
# import pandas
import pandas as pd
import csv

# import nfl suspension data
inputData = r'D:\udemy\Python Basics A-Z\data\nfl-suspensions-data.csv'
nfl_suspension = pd.read_csv(inputData, sep = ',')
nfl_suspension_list = list(csv.reader(open(inputData)))

# get year data into list years
year = list(nfl_suspension.loc[:,'year'].values)

# dictionnary with number of occurance per year
years = {}
for y in year:
    if y in years:
        years[y] += 1
    else:
        years[y] = 1

# get team data into list and unique that list
team = list(nfl_suspension.loc[:,'team'].values)
unique_team = set(team)

# get games data into list and unique that list
game = list(nfl_suspension.loc[:,'games'].values)
unique_game = set(game)

class Suspension():
    def __init__(self, data_frame, row):
        self.names = list(data_frame.loc[row:row,'name'].values)
        self.teams = list(data_frame.loc[row:row,'team'].values)
        self.games = list(data_frame.loc[row:row,'games'].values)
        try:    
            self.years = int(data_frame.loc[row:row,'year'].values)
        except:
            self.years = 0     
             
    def get_year(self):  
        return  self.years 


suspension = Suspension(nfl_suspension,22)    
missing_year = suspension.get_year()
print(missing_year)
