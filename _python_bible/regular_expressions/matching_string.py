import re

text = "test@mail.com"
result = re.fullmatch(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", text)
if result != None:
    print("Valid email")
else:
    print("Invalid email")
    

# IDENTIFIERS
# \d Some digit 
# \D Everything BUT a digit 
# \s White space 
# \S Everything BUT a white space 
# \w Some letter 
# \W Everything BUT a letter . Every character except for new lines 
# \b White spaces around a word 
# \. A dot

# MODIFIERS
# {1,3} We're expecting 1-3 digits
# + Match 1 or more
# ? Match 0 or 1
# * Match 0 or more
# $ Match the end of a string
# ^ Match the beginning of a string
# | Either or
# [] Range or "variance" [A-Z] [1-5]
# {x} Expecting "x" amount
