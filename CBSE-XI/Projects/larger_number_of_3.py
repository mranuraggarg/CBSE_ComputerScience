# Uses python3
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2020, CBSE Projects
# Input three numbers and display the largest / smallest number.

## Credits: CBSE

## License: GNU GPL v3.0
## Version: 1.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: stable
####################################################################################################

def larger_number_of_3(num1, num2, num3):
    """

    :param num1: int or float
    :param num2: int or float
    :param num3: int or float
    :return: largest and smallest int or float, tuple
    """
    if num1 < num2 < num3:
        return num3, num1
    elif num1 < num3 < num2:
        return num2, num1
    elif num2 < num1 < num3:
        return num3, num2
    elif num2 < num3 < num1:
        return num1, num2
    elif num3 < num2 < num1:
        return num1, num3
    elif num3 < num1 < num2:
        return num2, num3

a = 49
b = 50
c = 6

larger, smaller = larger_number_of_3(a, b, c)

print(f'largest number of {a}, {b} and {c} is {larger}')
print(f'smallest number of {a}, {b} and {c} is {smaller}')