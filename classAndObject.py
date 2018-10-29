# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:17:14 2018

Object et classe
Explain basics for objects and classes
Application in module with nfl.csv

@author: jacques
"""

class car():
    def __init__(self):
        self.color = 'black'
        self.mark = 'audi'
        self.modele = 'A4'

# example where we can define __ini__ function
class team():
    def __init__(self,name):
        self.name = name
        
    def print_name(self):
        print(self.name)

    
voiture = car()   
print(voiture.color)

man = team('Real Madrid')
man.print_name()