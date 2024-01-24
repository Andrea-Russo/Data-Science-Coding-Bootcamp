# -*- coding: utf-8 -*-
"""
Andrea Russo AR23110010747
T02 Challenge 1

"""
# Import necessary library
import math

# Warn the user to input positive numbers
print('In the following, insert only positive numbers')

# Request input of first side and store it as variable lenght1
len1=float(input('Please insert lenght of first side of triangle: '))

# Request input of second side and store it as variable lenght2
len2=float(input('Please insert lenght of second side of triangle: '))

# Request input of third side and store it as variable lenght3
len3=float(input('Please insert lenght of thrid side of triangle: '))

# The if condition checks if the triangle can be constructed from the inserted sides
if len1>len2+len3 or len2>len1+len3 or len3>len2+len1:
    # If the triangle is not valid, an error message is displayed
    print('The iserted side lenghts cannot form a triangle')
else:
    # If the triangle is valid, the area is computed
    
    # Compute semiperimeter
    s=(len1 + len2 + len3)/2
    # Compute area using semiperimeter
    area=round(math.sqrt(s*(s-len1)*(s-len2)*(s-len3)),3)
    
    # Print area
    print(f'The are of the triangle is {area}')


