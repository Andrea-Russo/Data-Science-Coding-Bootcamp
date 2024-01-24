"""
Andrea Russo AR23110010747
T12 Practical Task 1

"""
# Importing packages to make the program more interesting
import random as rnd

print('\nWelcome to the random cafe!\n')

# Define cafe menu as a list
menu = ['espresso','muffin','cake','juice','water']

# Define stock and price in apythonic way, I made it random to make it more interesting!
stock = {i:rnd.randint(0, 10) for i in menu} # Stock is an integer
price = {i:rnd.uniform(0.5, 5) for i in menu} # Price is a float

# Compute total_stock worth by creating and summing over the worth of each menu entry
total_stock = sum([stock[i]*price[i] for i in menu])

# Use format string to present result, rounding to 2 decimanls in the most pythonic way
print(f'The total stock value of the cafe is: {total_stock:.2f}£')





