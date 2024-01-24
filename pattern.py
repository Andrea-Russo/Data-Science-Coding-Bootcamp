"""
Andrea Russo AR23110010747
T08 Practical Task 1

"""
# Insert maximum number of starts printed
max_stars = 5

# Using a single for loop to manage both the ascending and descending parts
for i in range(1, max_stars*2):
    if i <= max_stars:
        # First half (ascending)
        print('*' * i)
    else:
        # Second half (descending)
        print('*' * (max_stars*2 - i))
