#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 11:03:41 2018

@author: jdelfrate
"""


import time
import datetime

# time.time()
current_time = time.time()
print(current_time)

# time.gmtime()
current_struct_time = time.gmtime()
print(current_struct_time)

# how to select info in current_struct_time
current_hour = current_struct_time.tm_hour
print(current_hour)
current_year = current_struct_time.tm_year
print(current_year)

# datetime.now()
current_datetime = datetime.datetime.now()
current_year = current_datetime.year
print(current_year)
current_month = current_datetime.month
print(current_month)

# classe timedelta
today = datetime.datetime.now()
diff = datetime.timedelta(weeks = 1, days = 5)
print(today)
print(diff)
print(today + diff)

# Formater date
# datetime.strftime()
str_today = today.strftime('%b,%d,%y')
print(str_today)
# strptime()
today_2 = time.strptime(str_today, '%b,%d,%y')
print(today_2)