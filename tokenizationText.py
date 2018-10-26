# -*- coding: utf-8 -*-
"""
This script load data and clean special character

Created on Thu Oct 25 23:51:03 2018

@author: Jacques Delfrate
"""

def spell_check(inputText, inputVoc, special_characters, replacement_string):
    """ read """
    misspelled_word = []
    string     = open(inputText, 'r', encoding = 'utf-8').read()
    vocabulary = open(inputVoc, 'r', encoding = 'utf-8').read()
    """ Tokenize """
    tokenized_texte = tokenize(string, special_characters, replacement_string, True)
    tokenized_voc   = tokenize(vocabulary, special_characters, replacement_string, True)    
    """ Check if text is in the vocabulary """
    for iToken in tokenized_texte:
        if iToken not in tokenized_voc and iToken != '':
            misspelled_word.append(iToken)            
    return misspelled_word

def tokenize(string_value, special_character, replacement_string, clean = False):
    cleaned_text = string_value
    if clean:
        cleaned_text = clean_text(string_value, special_character, replacement_string)  
    text_tokens = cleaned_text.split(" ")
    return text_tokens

def clean_text(string_value, special_character, replacement_string):
    for iSpecial in special_character:
        string_value = string_value.replace(iSpecial, replacement_string)
    string_value = string_value.lower()
    return string_value
    

""" Def """
inputText = r'D:\udemy\Python Basics A-Z\data\texte.txt'
inputVoc  = r'D:\udemy\Python Basics A-Z\data\dictionnaire.txt'
special_characters = [".",",","'", "\n"]
replacement_string = ""


""" Test """
misspelledWord = spell_check(inputText, inputVoc, special_characters, replacement_string)

print(misspelledWord)
    
""" Argument multiple 
        Change two strings in on sentence """
def modify_string(sentence2change, string1, string2):
    new_sentence = sentence2change.replace(string1, string2)
    return new_sentence