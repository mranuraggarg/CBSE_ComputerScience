# Uses python3
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2020, CBSE Projects
# Input two numbers and display the larger / smaller number.

## Credits: CBSE

## License: GNU GPL v3.0
## Version: 1.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: stable
####################################################################################################

def larger_number(num1, num2):
    """

    :param num1: int or float
    :param num2: int or float
    :return: sorted tuple
    """
    if num1 > num2:
        return num1, num2
    else:
        return num2, num1

a = 4
b = 5

larger, smaller = larger_number(a, b)

print(f'larger number of {a} and {b} is {larger}')
print(f'smaller number of {a} and {b} is {smaller}')
