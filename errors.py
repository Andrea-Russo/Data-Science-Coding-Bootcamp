"""
Andrea Russo AR23110010747
T09 Practical Task 1

"""
print("Welcome to the error program") # SyntaxError: missing parenthesis
print("\n")     # IndentationError: code block needs to start from begin. SyntaxError: missing parenthesis

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" # RuntimeError: age_Str needs to be declare, while a logical operator is used
age = int(age_Str[:2]) # RuntimeError: Now the age is converted just from the numerical part of age_Str
print(f"I'm {age} years old.") # RuntimeError: Implemented formst string to display result correctly

# Variables declaring additional years and printing the total years of age
years_from_now = "3" 
total_years = age + int(years_from_now)  # TypeError: fixed by converting string into int

print(f'The total number of years: {total_years}') # SyntaxError: missing parenthesis. Print statement fixed with format string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12  # NameError: fixed by replacing total with correct variable name
print(f"In 3 years and 6 months, I'll be {total_months+6} months old") # SyntaxError: missing parenthesis. LogicError: 6 months were missing to the count.

#HINT, 330 months is the correct answer

