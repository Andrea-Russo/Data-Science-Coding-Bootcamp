"""
Andrea Russo AR23110010747
T07 Practical Task 1

"""
# Create variables to track total sum and number of inputs
total_sum = 0
number_count = 0

# Request user input and append to list
num = float(input('Please insert a number: '))

# If the first inserted number is not -1, keep asking until -1 is inserted
if num == -1:
    average = 0 # Average is 0 if the inserted number is immediately -1
else:
    while num != -1:
        # For each iteration, the sum and counter are updated
        total_sum += num
        number_count += 1
        num = float(input('Please insert another number: '))
    
    # Average is compute when -1 is inserted
    average = total_sum / number_count
    
print(f'The average of the numbers inserted before -1 is {average}.')
