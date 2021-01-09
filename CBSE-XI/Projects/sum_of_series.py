# Uses python3
##################################################
## For detail refer README.md in the main folder
##################################################
## GNU General Public License v3.0
##################################################
## Author: ANURAG GARG
## Copyright: Copyright 2020, CBSE Projects
# Write a program to input the value of x and n and print the sum of the
# following series:
# 1. x**n
# 2. (-1**n)x**(n)
# 3. (-1**n)x**(n)/n 0 < n <= n
# 4. x**n / n!

## Credits: CBSE

## License: GNU GPL v3.0
## Version: 1.1.0
## Mmaintainer: ANURAG GARG
## Email: mranuraggarg@yahoo.com
## Status: stable
####################################################################################################
import math


# 1. x**n
def sum_of_series_1(x, n):
    """
    series nth term: x**n
    :param x: int
    :param n: int
    :return: sum of series
    """
    # Geomertic progression series: a + ax + ax**2 + ... + ax**n
    # a = 1
    # r = x
    # number_of_terms = n

    return (1 - x ** (n+1)) / (1 - x)

# Checking the sum of series for n = 7 x = 2 nth term = 128
assert sum_of_series_1(2, 7) == 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128

print(f'Sum of first series for x = 2 and n = 7 is {sum_of_series_1(2, 7)}')

# 2. (-1**n)x**(n)
def sum_of_series_2(x, n):
    """
    series nth term: (-1**n) x**(n)
    :param x: int
    :param n: int
    :return: sum of series
    """
    # Geomertic progression series: a - ax + ax**2 - ax**3 + ... + ax**n
    # a = 1
    # r = x
    # number_of_terms = n
    m_pos = math.ceil((n + 1) / 2)
    m_neg = math.floor((n + 1) / 2)
    y = x**2 # Common ratio has changed from x -> x**2
    sum_pos = (1 - y ** m_pos) / (1 - y)
    sum_neg = (-x) * (1 - y ** m_neg) / (1 - y)
    return sum_pos + sum_neg

# Checking the sum of series for n = 7 x = 2 nth term = 128
assert sum_of_series_2(2, 7) == 1 - 2 + 4 - 8 + 16 - 32 + 64 - 128

print(f'Sum of second series for x = 2 and n = 7 is {sum_of_series_2(2, 7)}')


# 3. (-1**(n+1))x**(n)/n 0 < n <= n
def sum_of_series_3(x, n):
    """
    series nth term: (-1**n) x**(n)
    :param x: int
    :param n: int
    :return: sum of series
    """
    # number_of_terms = n
    # Partial sum of n terms
    if n == 0:
        result = 0.0
    elif n == 1:
        result = x
    else:
        result = x + x**2 / 2
        for m in range(3, n+1):
            term = (-1)**m * x**m / m
            result += term
    return result

# Checking the sum of series for n = 7 x = 2 nth term = 128/7
assert sum_of_series_3(2, 7) == 2 + 4/2 - 8/3 + 16/4 - 32/5 + 64/6 - 128/7

print('Sum of third series for x = 2 and n = 7 is {:.2f}'.format(sum_of_series_3(2, 7)))


# 4. x**n / n!
def fact(num):
    if num > 1:
        result = 1
        for i in range(1, num+1):
            result *= i
    return result


def sum_of_series_4(x, n):
    """
    series nth term: (-1**n) x**(n)
    :param x: int
    :param n: int
    :return: sum of series
    """
    # number_of_terms = n
    # Partial sum of n terms
    if n == 0:
        result = 0.0
    elif n == 1:
        result = x
    else:
        result = x + x**2 / 2
        for m in range(3, n+1):
            term = (-1)**m * x**m / fact(m)
            result += term
    return result

# Checking the sum of series for n = 7 x = 2 nth term = 128/7
assert sum_of_series_4(2, 7) == 2 + 4/2 - 8/6 + 16/24 - 32/120 + 64/720 - 128/5040

print('Sum of fourth series for x = 2 and n = 7 is {:.2f}'.format(sum_of_series_4(2, 7)))
