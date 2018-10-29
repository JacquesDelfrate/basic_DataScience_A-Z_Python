# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 18:04:20 2018

Module class and boolean
And, or, ==
First class and object implementation

@author: jacques
"""
#import numpy as np
import pandas as pd

# Path
inputNFL = r'D:\udemy\Python Basics A-Z\data\NFL.csv'

# read csv file and convert list
#nflData_list = pd.read_csv(inputNFL, sep=',').values.tolist()
# convert NFL data to list
#nflData_list = nflData.values.tolist()

class Team():
    ''' init class Team '''
    def __init__(self,team_name,year,inputNFL):
        self.name = team_name
        self.year = year
        self.nflData = pd.read_csv(inputNFL, sep=',').values.tolist()
        self.count_victory_total = 0
        self.count_victory_year = 0
    
    ''' print count '''
    def print_name(self, flag = False):
        if flag:
             print(self.count_victory_year)           
        else:
            print(self.count_victory_total)
            print(self.count_victory_year)

    ''' count how many time a team won '''
    def nbVictory_count_total(self):
        for iRow in self.nflData:
            if self.name in iRow[2]:
                self.count_victory_total+=1
        return  self.count_victory_total
    
    ''' count how many time a team won in a year '''
    def nbVictory_count_year(self):
        for iRow in self.nflData:
            if iRow[0] == self.year and self.name in iRow[2]:
                self.count_victory_year+=1
        return self.count_victory_year 

      
# Variables init
team_name = 'San Francisco 49ers'
year = 2013
flag = True

# class Team
SF = Team(team_name,year,inputNFL)

# Compute total number of victory from class Team
SF_wins_total = SF.nbVictory_count_total()

# Compute number of victory in 2013
SF_wins_year = SF.nbVictory_count_year()

# print results for 2013 (flag = True)
SF.print_name(flag)


'''
np.sqrt(25)
np.ceil(23.4)
np.floor(23.4)

print(np.pi)

# print NFL data list
print(nflData_list) 

a = 5
b = 10

a<5
b>5

print(a<5 or b>5)
print(a<5 and b>5)


'''

