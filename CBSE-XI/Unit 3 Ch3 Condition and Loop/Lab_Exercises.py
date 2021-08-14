# Q1
# answer = raw_input("Do you like Python? ") if answer == "yes":
# print "That is great!" else:
# print "That is disappointing!"

# Modify the program so that it answers "That is great!" if the answer was "yes", "That is disappointing" if the answer
# was "no" and "That is not an answer to my question." otherwise.

def exercise_1():
    answer = raw_input("Do you like Python? ")

    if answer == "yes":
        print("That is great!")
    else:
        print("That is disappointing!")


# Q2
# Write a function to find whether given number is odd or even.

def exercise_2(num):
    return "even" if num % 2 == 0 else "odd"


# Q3
# Print all multiples of 13 that are smaller than 100. Use the range function in the following manner:
# range (start, end, step) where "start" is the starting value of the counter, "end" is the end value
# and "step" is the amount by which the counter is increased each time.

def exercise_3():
    for num in range(13, 101, 13):
        print(num)


# Q4
# Write a program using while loop that asks the user for a number, and prints a countdown from that number to zero.
# Note: Decide on what your program will do, if user enters a nExampleative number.

def exercise_4():
    num = int(input("Enter an integer - "))

    if (num < 0):
        print("Entered number is negative, please enter positive number")
        exercise_4()

    while num >= 0:
        print(num)
        num -= 1


# Q5
# Using for loop, write program that prints out the decimal equivalent of 1⁄2, , 1⁄4, -- ---- 1/10,

def exercise_5():
    for num in range(2, 11, 2):
        print(1/num)

