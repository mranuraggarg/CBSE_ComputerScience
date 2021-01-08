"""
Python 3
Computer Science
Grade 11
NCERT Problems
Page no: 126
"""
import math

# Q5 Write the code to show all the 6 math functions
# +, -, *, /, %, //
a = 5 + 6
b = 6 - 5
c = 6 / 4
d = 6 % 2
e = 7 // 2
print(f'Q5: Use of all the 6 math functions\n5 + 6 = {a}',
      f'\n6 - 5 = {b}',
      f'\n6 / 4 = {c}',
      f'\n6 % 2 = {d}',
      f'\n7 // 2 = {e}')

# Q6 Write a code that prints your full name and your Birthday as separate strings.
name = 'Anurag Garg'
dob = '09/03/1983'
print(f'\nQ6\nMy name is {name} and dob is {dob}')

# Q7 Write a program that asks two people for their names;
# stores the names in variables called name1 and name2; says hello to both of them.
name1 = input('\nQ7\nEnter the name of first Person: ')
name2 = input('Enter the name of second Person: ')
print(f'\nHello!, {name1} and {name2}')


# Q8 Calculate root of the following equation
# a) 34x**2 + 68x - 510 = 0
# b) 2x**2 - x - 3 = 0

# Functions to calculate the roots:
def roots(a, b, c):
    """
    :param a: int or float
    :param b: int or float
    :param c: int or float
    :return: tuple
    """
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        discriminant = math.sqrt(discriminant)
        root1, root2 = (-b + discriminant) / (2 * a), (-b - discriminant) / (2 * a)
    else:
        root1, root2 = 'No real Roots', None
    return root1, root2


# Roots for equation a)
a1 = 34
b1 = 68
c1 = -510
x1, x2 = roots(a1, b1, c1)
print(f'\nQ8 a)\nRoots for 34x**2 + 68x - 510 = 0 are: \n{x1} and {x2}')

a2 = 2
b2 = -1
c2 = -3
x1, x2 = roots(a2, b2, c2)
print(f'\nQ8 b)\nRoots for 2x**2 - x - 3 = 0 are: \n{x1} and {x2}')
