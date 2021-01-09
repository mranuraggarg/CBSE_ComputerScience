# Uses python3
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2020, CBSE Projects
# Given two integers x and n, compute 𝑥**n.

## Credits: CBSE

## License: GNU GPL v3.0
## Version: 1.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: stable
####################################################################################################

def pow_n(x, n):
    """

    :param x: int or float
    :param n: int
    :return: int or floar
    """
    result = 1
    if n >= 1:
        result = x
        for _ in range(1, n):
            result *= x
    return result

num1 = 2
exponent = 0

print(f'{num1} raised to power {exponent} is\n {pow_n(num1, exponent)}')