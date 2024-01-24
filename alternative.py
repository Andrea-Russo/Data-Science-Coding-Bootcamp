"""
Andrea Russo AR23110010747
T11 Practical Task 11

"""
# Request user input string
string = input('Please insert a string: ')

# Prepare output strings. One is an empty string, the other is the input string split into words
alter_char = ''
alter_word = string.split()

# Run through the string characters, and add letters with alternating cases to alter_char
for i in range(len(string)):
    if i % 2 == 0:
        alter_char += string[i].upper()
    else:
        alter_char += string[i].lower()
        
# For each word in the split string, alternate between lowering and raising words
for i in range(len(alter_word)):
    if i % 2 == 0:
        alter_word[i] = alter_word[i].lower()
    else:
        alter_word[i] = alter_word[i].upper()

# Print results. For the second string, join words with black spaces
print(alter_char)
print(' '.join(alter_word))
