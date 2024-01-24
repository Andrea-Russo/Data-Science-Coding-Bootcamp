# -*- coding: utf-8 -*-
"""
Andrea Russo AR23110010747
T02 Practical Task 1

"""

# Importing stext sentence
sentence='The!quick!brown!fox!jumps!over!the!lazy!dog'

# Replacing charcters '!' with blanck space and reprinting
sentence=sentence.replace('!',' ')
print(sentence)

# Transforming into uppercase and reprinting
sentence=sentence.upper()
print(sentence)

# Printing in reverse usign slicing
print(sentence[::-1])