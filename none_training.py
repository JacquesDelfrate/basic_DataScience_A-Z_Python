#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 12:33:08 2018

Training for None
Parcourir values
vérifier si la valeur est différente de None et plus grande que 30
Ajouter la valeur a une list check si c'est le cas à la de la compréhensino de liste
Afficher check

@author: jdelfrate
"""

values = [None, 1, 45, None, 75]

check = [value != None and value > 30 for value in values] 
     
print(check)