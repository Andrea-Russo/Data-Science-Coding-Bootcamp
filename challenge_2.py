# -*- coding: utf-8 -*-
"""
Andrea Russo AR23110010747
T02 Challenge 2

"""

# Request name of user's favourite restaurant and store it in string_fav
string_fav=input('Please insert name of favourite restaurant: ')

# Request user's favourite number and store it in int_fav
int_fav=int(input('Please insert favourite integer: '))

# Print both variables
print(f'The user favourite restaurant is {string_fav}')
print(f'The user favourite integer is {int_fav}')


int(string_fav)
# When trying to cast string_fav as in an integer we get the error
#  invalid literal for int() with base 10:'string_fav'. This isbacause the string 
#  is not the representation of a base 10 integer and hence cannot be casted into one.
