"""
Andrea Russo AR23110010747
T09 Optional Challenge

"""


# Compilation error 1: Syntax error due to missing quotes around string
print(Welcome to the error-filled program!)

# Initializing a list
numbers = [1, 2, 3, 4, 5]

# Runtime error: IndexError due to accessing an index out of range
print("This will cause an error:", numbers[5])  # Index 5 does not exist in 'numbers'

# Compilation error 2: Syntax error due to undefined variable (num instead of number)
sum = 0
for number in numbers:
    sum += num

# Logical error: Incorrect calculation of average
# It should divide the sum by the length of the list, not by a fixed number
average = sum / 10  
print("Average of numbers:", average)  # This will print an incorrect average

