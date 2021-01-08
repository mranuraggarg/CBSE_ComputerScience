"""
Python 3
Computer Science
Grade 11
NCERT Problems
Page no: 151
"""
import math


# Q3 Write a script that asks a user for a number.
# Then adds 3 to that number,
# and then multiplies the result by 2,
# subtracts twice the original number,
# then prints the result.

def math_operations():
    """
    :param: x: int or float
    :return: int
    """
    x = float(input('Enter any real number: '))
    return int((x + 3) * 2 - 2 * x)


print(f'Q3\n{math_operations()}')


# Q4 In analogy to the example,
# write a script that asks users for the temperature in F and prints the temperature in C.
# (Conversion: Celsius = (F - 32) * 5/9).

def f_to_c():
    """
    :return: float
    """
    f_temp = float(input('\nQ4\nEnter the temperature in F '))
    return (f_temp - 32) * 5 / 9


print(f'Temperatur in Celcius is {f_to_c()}')


# Q5 Write a Python function, odd, that takes in one number
# and returns True when the number is odd and False otherwise.
# You should use the % (mod) operator, not if.

def odd(num):
    """

    :param num: int
    :return: boolean
    """
    return num % 2 == 1


print(f'\nQ5\n{odd(11)}')


# Q6 Define a function "SubtractNumber(x,y)‟ which takes in two numbers and
# returns the difference of the two.

def SubtractNumber(x, y):
    """

    :param x: int or float
    :param y: int or float
    :return: int or float
    """
    return x - y


print(f'\nQ6: \n{SubtractNumber(3, 5)}')


# Q7 Write a Python function, fourthPower( ),
# that takes in one number and returns that value raised to the fourth power.

def fourthPower(num):
    """

    :param num: int or float
    :return: int or float
    """
    return num ** 4


print(f'\nQ7: \n{fourthPower(3)}')


# Q8 Write a program that takes a number and calculate and display
# the log, square, sin and cosine of it.

def calulate_log_sin_cos(num):
    """

    :param num: int or float
    :return: None
    """
    print('\nQ8')
    print(f'logorithm of {num} with base 10 is {math.log(num, 10)}')
    print(f'sine of {num} is {math.sin(num)}')
    print(f'cosine of {num} is {math.cos(num)}')
    return None


calulate_log_sin_cos(10)
