# -*- coding: utf-8 -*-
"""
Andrea Russo AR23110010747
T02 Practical Task 2

"""
# Ask user for input sentence
str_manip=input('Please insert a sentence: ')

# Print sentence lenght
print(len(str_manip))

# Finding last letter and substituting everywhere with '@'
print(str_manip.replace(str_manip[-1],'@'))

# Print last 3 charcters backwards
print(str_manip[-3:][::-1])

# Create 5 letter word made of first three and last two characters
print(str_manip[:3]+str_manip[-2:])