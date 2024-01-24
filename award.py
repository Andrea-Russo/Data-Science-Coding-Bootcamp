"""
Andrea Russo AR23110010747
T04 Practical Task 1

"""

# Request user for number of minutes of each triathlon competition and store it.
# Input is assumed to be an integer.
swim_minutes = int(input('Please insert the number of minutes for swimming: '))
cycling_minutes = int(input('Please insert the number of minutes for cycling= '))
run_minutes = int(input('Please insert the number of minutes for running: '))

# Calculate and display total time taken
total = swim_minutes+cycling_minutes+run_minutes
print(f'The total time taken is {total} minutes')

# Find appropriate award and display it
if total <= 100:
    print('You are awarded Provincial Colours!')
elif 100 < total <= 105:
    print('You are awarded Provincial Half Colours!')
elif 105 < total <= 110:
    print('You are awarded Provincial Scroll!')
else:
    print('Sorry, no award for you.')