# -*- coding: utf-8 -*-
"""
Andrea Russo T01
Practical Task 2

"""
# Pseudo code
# -request string input from the user for their name 
# -store input into a variable called 'name'
# -request string input from the user for their age 
# -store input into a variable called 'age'
# -request string input from the user for their house number 
# -store input into a variable called 'house_number'
# -request string input from the user for their street name 
# -store input into a variable called 'street_name'
# -use an f string to print the stored variables by composing a simple sentence

# Request name, age, house number and street number
name=input('Insert name: ')
age=input('Insert age: ')
house_number=input('Insert house number: ')
street_name=input('Insert street name: ')

# Print variables using an f string and combining them in a sentence
print(f'The person named {name} lives at house number {house_number} on {street_name}. This person is {age} years old.')