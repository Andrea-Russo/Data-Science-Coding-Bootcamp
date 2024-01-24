"""
Andrea Russo AR23110010747
T09 Practical Task 1

"""

animal = 'Lion' # NameError: fixed variable to be a string like intended
animal_type = "cub"

# Fixed logical error: a Lion cub hs 30 teeth: https://leofoundation.org/wp-content/uploads/2017/01/lion_aging-brochure-2010.pdf
number_of_teeth = 30

# LogicalError: inserted variables in the correct place and turned the string into a format string
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth."

print(full_spec)  # SyntaxError: inserted missing parenthesis

