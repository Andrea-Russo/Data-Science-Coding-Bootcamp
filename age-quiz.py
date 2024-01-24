# -*- coding: utf-8 -*-
"""
Andrea Russo AR23110010747
T03 Practical Task 1

"""

# Request age of user and store in integer variable
age = int(input('Please insert your age: '))

# The if condition now checks the age. 
# Since the conditions are checked in descending order, this combination alloows
#  for the least complex logical conditions.
if age > 100:
    print("Sorry, you're dead.")
elif age > 65:
    print('Enjoy your retirement!')
elif age > 40:
    print("You're over the hill.")
elif age == 21:
    print('Congrats on your 21st!')
elif age < 13:
    print('You qualify for the kiddie discount.')
else:
    print('Age is but a number.')