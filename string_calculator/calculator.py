#----------------------------------------------------------------------------------------------
# STRING CALULATOR PROGRAM USING TDD
#
# INSTRUCTIONS
# 1. Create an add function that can handle up to two integers passed in as a string.
# 2. Modify the add function to handle multiple integers.
# 3. Modify the add function so that it can handle new lines between integers
# 4. Modify the add function so that it can handle different delimeters
# 5. Modify the add function so that it can handle negative integers.
# 6. Modify the add function so that it ignores integers greater than or equal to 1000.
# 7. Modify the add function so that it can support delimiters of any length
# 8. Modify the add function so that it is able to support different delimiters of any length
# 9. Modify the add function so that it can handle invalid input.
#----------------------------------------------------------------------------------------------

# Import regular expression to form a search pattern
#import re

# Add function
def add(string):
    if len(string) == '':
        return 0
    elif len(string) == 1:
        return int(string)
    elif string[0] == "/":
        result = 0
        delim = ""
        lines = string.split("\n")
        for char in range(2, len(lines[0])):
            delim = delim + lines[0][char]
        integers = lines[1].split(delim)
        return multipleIntegers(integers)
    
    else:
        result = 0
        delim = ","
        if string [1] != ",":
            delim = "\n"
        integers = string.split(delim)
        return multipleIntegers

# Function to calculate multiple integers
def multipleIntegers(integers)
    result = 0
    for integer in integers:
        result += int(integer)
    return result