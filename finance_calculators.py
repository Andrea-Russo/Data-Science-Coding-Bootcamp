"""
Andrea Russo AR23110010747
T05 Capstone Project

"""
# Importing necessary library
import math


# Present menu of choices
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond       - to calculate the amount you'll haver to pay on a home loan.")

# Ask user for choice from menu
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# dpending on the user choice, the task is carried on
if choice == 'investment':
    # Notify user of choice
    print('You chose the investment calculator.')
    
    # Ask user for principal amount, yearly rate of interest, tears of investing and type of interest and store them
    principal = float(input('Insert amount of money to invest: '))
    rate = float(input('Insert the yearly interest rate as percentage (ex. 1.5 for 1.5%): ')) / 100
    years = float(input('Insert the number of years planned for investing: '))
    
    # If a negative number is inserted, the program asks for them again until corrected
    while principal <0 or rate <0 or years <0:
        print('Negative numbers are not allowed, please insert again.')
        principal = float(input('Insert amount of money to invest: '))
        rate = float(input('Insert the yearly interest rate as percentage (ex. 8 or 1.5): ')) / 100
        years = float(input('Insert the number of years planned for investing: '))
        
    # Request choice of interest from user until a correct choice is inserted
    interest = input("Insert 'simple' for simple interest or 'compound' for compound interest: ").lower()
    while interest != 'simple' and interest != 'compound':
        print('Choice of interest not valid')
        interest = input("Insert 'simple' for additive interest or 'compound' for coumpound interest: ").lower()
    
    # Compute investments after the inserted years and print it
    if interest == 'simple':
        tot = round(principal * (1 + rate*years),2)
        print(f'After {years} years, the final investment will amount to ${tot}.')
    elif interest == 'compound':
        tot = round(principal * (1 + rate)**years,2)
        print(f'After {years} years, the final investment will amount to ${tot}.')
    
    # As an extra, compute and print investments return
    ret = round(100 * (tot - principal) / principal,2)
    print(f'The return on your investment will be {ret}%.')
    
elif choice == 'bond':
    # Notify user of choice
    print('You chose the bond calculator.')
    
    # Request present house value, yearly interest rate, months planned to to repay loan and store them.
    house = float(input('Insert the present value of the house: '))
    rate = float(input('Insert the yearly interest rate as percentage (ex. 1.5 for 1.5%): ')) / 1200
    months = int(input('Insert the number of months planned for repaying the bond: ')) # Since loan repayments are monthly, this is assumed to be an integer.
    
    # If a negative number is inserted, the program asks for them again until corrected
    while house < 0 or rate < 0 or months < 0:
        print('Negative numbers are not allowed, please insert again.')
        house = float(input('Insert the present value of the house: '))
        rate = float(input('Insert the yearly interest rate as percentage (ex. 1.5 for 1.5%): ')) / 1200 # Converted to monthly rate
        months = int(input('Insert the number of months planned for repaying the bond: '))
    
    #Compute and display monthly payment
    monthly = round((rate * house) / (1 - (1 + rate)**(-months)),2)
    print(f'The monthly repayment to estinguish the loan in {months} months is ${monthly}.')
    
else:
    print('Choice not valid, start the program again and select a choice from the menu.')