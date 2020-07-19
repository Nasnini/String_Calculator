from string_calculator.calculator import add

#import pytest

# Testing invalid inputs
# def test_invalid_input():
#     assert add(string) == "invalid input"

# Testing id add function is 0
def test_add_empty_str():
    assert add("") == 0

# Testing that the add function has one value
def test_add_one_integer():
    assert add("1") == 1

# Testing that the add function has two values
def test_add_two_integers():
    assert add("1,2") == 3

# Testing the add function can have multiple integers
def test_add_many_integers():
    assert add("1,2,3,4") == 10 

# Testing if add can handle new lines between integers instead of commas
def test_new_lines():
    assert add("1\n2,3") == 6

# Testing different delimeters
def test_diff_delimiters():
    assert add("//;\n1;2") == 3

# Testing if there are negatives values
def test_check_negatives():
    with pytest.raises(Exception) as err:
        assert add("//;\n-1;2,-3")
        assert str(err.value) == "Negatives not allowed: -1,-3,"    

# Testing if any number bigger than 20 will be ignored
def test_more_than_twenty():
    assert add("//;\n1;2,21") == 3

# Testing if delimeters can be of any length
def test_delimeter_len():
    assert add("//[***]\n1***2***3") == 6

# Testing if the add function can allow multiple delimeters
def test_multiple_delimeters():
    assert add("//[*][%]\n1*2%3") == 6

