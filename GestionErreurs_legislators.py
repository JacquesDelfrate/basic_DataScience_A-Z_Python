# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 00:08:00 2018

Gestion des erreurs section

@author: jacques
"""

# library
import pandas as pd
import platform

plt_node = platform.node()
# init variables
if plt_node == 'megawatt':
    inputData = r'/home/jdelfrate/Documents/basics_python_data/legislators.csv'
    outputData = r'/home/jdelfrate/Documents/basics_python_data/output_legislators.csv'
    gender_nan = 'M'
    party_nan = 'No party'
else:
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
# extract first_name
first_name = list(legislator.loc[:,'first_name'].values)


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

# Compute how many F
# Empty dictonnary
name_counts = {}
# go throught gender and birth year at the same time
for x, genre in enumerate(gender):
    # if gender is F and birth year more than 1950
    if genre == 'F' and birth_year[x] > 1950:
        # set first-name into variables
        name = first_name[x]
        # check if first name already in dictionnary
        if name in name_counts: # if in the dictionnary count +1
            name_counts[name]+=1
        else: # if not add this first name to the dictionnary
            name_counts[name]=1
# print output count
print(name_counts)   

# Extract the biggest F first name count from dictionnary name_counts
# print result
# from the course
max_value = None
for k in name_counts:
    count = name_counts[k]
    if max_value is None or count > max_value:
        max_value = count
print(max_value)
# in house --> two lines of code instead of for loop and if condition
  # max(name_counts, key=name_counts.get) get the name where the count is max (they are several but select one)
  # get the value for the name where is max is
max_value = name_counts[max(name_counts, key=name_counts.get)]
print(max_value)

# extract first name with max_value occurance
# gives boolean false true if number = 2 (max occurence)
f_name = [number == max_value for name, number in name_counts.items()]
# what we want
f_name = [name for name,number in name_counts.items() if number == max_value]
print(f_name)


# Training
  # 

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
    
# enumerate()
students = ['Anna', 'Martin', 'Bob', 'Eric', 'Elise']    
ages = [16, 15, 18, 20, 20]
for i, student in enumerate(students):
    print(student)
    print(ages[i])
    
cars = [['noir', 'Peugeot', '308'], ['blanche', 'audi', 'A4']]
price = [23000,49000]
for i, car in enumerate(cars):
    car.append(price[i])
print(cars)

# Compréhension de liste
animals = ['chien', 'chat', 'vache', 'panda', 'tigre']
animal_length = []
for animal in animals:
    animal_length.append(len(animal))
print(animal_length)

animal_length_2 = [len(animal) for animal in animals]
print(animal_length_2)

prices = [10,45,156,7800]
prices_doubles = [price*2 for price in prices]
print(prices_doubles)

# none
max_value = None
for k in name_counts:
    count = name_counts[k]
    if max_value is None or count > max_value:
        max_value = count
print(check)        

values = [None, 1, 45, None, 75]
check = [value != None and value > 30 for value in values]     
print(check)
    
# items()
fruits = {'Orange': 12, 'Banana': 5, 'Kiwi': 6}
for fruit, number in fruits.items():
    print(fruit)
    print(number)
'''


