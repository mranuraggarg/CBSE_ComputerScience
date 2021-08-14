"""
Python 3
Computer Science
Grade 11
NCERT Problems
Page no: 151
"""
import random

# Q9 a) Write a program, to display a tic-tac-toe board on screen, using print statement.

print(f'x\to\tx')
print(f'x\to\to')
print(f'o\to\tx')

# Q9 b) Write a program to display a tic-tac-toe board on screen using variables,
# so that you do not need to write many print statements?
print(f'Q9 b) ----------------------')
line = f'x\to\tx'
for _ in range(3):
    print(line)

# Q10 Write a function roll_D ( ), that takes 2 parameters-
# the no. of sides (with default value 6) of a dice, and
# the number of dice to roll-and generate random roll values for each dice rolled.
# Print out each roll and then return one string “That‟s all”.
# Example roll_D (6, 3)
# 4
# 1
# 6
# That‟s all


def roll_D(roll, sides=6):
    """

    :param sides: int
    :param roll: int
    :return: None
    """
    for _ in range(roll):
        print(random.randint(0, sides))

    return None


print(f'Q10 --------------------------')
roll_D(sides=6, roll=3)
