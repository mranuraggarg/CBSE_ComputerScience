'''
Python 3
Computer Science
Grade 11
NCERT Problems
Page no: 150
'''

# Q1 Write a program to ask for following as input
# Enter your first name: Rahul
# Enter your last name: Kumar
# Enter your date of birth
# Month? March
# Day? 10
# Year? 1992
# And display following on screen
# Rahul Kumar was born on March 10, 1992.

f_name = input('Enter your first name: ')
l_name = input('Enter your last name: ')
print('Enter your date of birth: ')
month = input('Month? ')
day = input('Day? ')
year = input('Year? ')
print(f'{f_name} {l_name} was born on {month} {day}, {year}.')

# Q2
def intDiv (x, a):
    """

    :param x: a non-negative integer argument
    :param a: a positive integer argument
    :return: integer, the integer division of x divided by
    """
    assert x > 0 and isinstance(x, int)
    assert a > 0 and isinstance(a, int)
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

print(intDiv(5, 3))