# Import regular expression to form a search pattern
import re

# Constructor to compile the regular expression
regex = re.compile(r'\d+')

# Method to check empty string values
def has_negatives(string):
    empty_string = ''

    # For loop to search a specific search pattern
    for x in range(len(string)):
        if string[x] == '-' and string[x+1].isdecimal():
            empty_string += '-' + string[x+1] + ','

    return empty_string

# Add function 
def add(string):
    sum = 0
    numbers = regex.findall(string) # Find all regular expressions
    negatives = has_negatives(string)
    
    # Try this to check if theres any negative numbers, else raise an exception and print error message
    try:
        string[:-1]
    except:
        raise "This is not ok!"
    if negatives:
        raise Exception("Negatives are not allowed: " + negatives)

    #If theres an empty string: return 0, else continue checking...
    if string == '':
        return 0
    else:
        for x in numbers:
            # Program is limited to 20 values in this case
            if int(x) > 20:
                pass
            else:
                num = int(x)
                sum += num
        # return sum on the calculator
        return sum
print(add("1,1"))
