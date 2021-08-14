# Write a program that takes a number and calculate and display the log, square, sin and cosine of it.

# import log, sin and cos functions from library math
from math import log, sin, cos

def calculate_functions(num: int):
    # To be able to calculate log
    # num should be positive
    assert num > 0

    return round(log(num), 4), num**2, round(sin(num), 4), round(cos(num), 4)

if __name__ == "__main__":
    # Print (2.302585092994046, 100, -0.5440211108893699, -0.8390715290764524
    print(calculate_functions(10))

