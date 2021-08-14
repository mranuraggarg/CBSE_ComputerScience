# Q1
# answer = raw_input("Do you like Python? ") if answer == "yes":
# print "That is great!" else:
# print "That is disappointing!"

# Modify the program so that it answers "That is great!" if the answer was "yes", "That is disappointing" if the answer
# was "no" and "That is not an answer to my question." otherwise.

def exercise_1():
    answer = input("Do you like Python? ")

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
    num = int(input("Enter an integer - "))  # type: int

    if num < 0:
        print("Entered number is negative, please enter positive number")
        exercise_4()

    while num >= 0:
        print(num)
        num -= 1


# Q5
# Using for loop, write program that prints out the decimal equivalent of 1/2, , 1/4, -- ---- 1/10,

def exercise_5():
    for num in range(2, 11, 2):
        print(1/num)


# Q6
# Write a function to print the Fibonacci Series up to an Input Limit.

def exercise_6():
    num = int(input("Enter a limiting integer - "))  # type: int

    fibo = 0
    fibo1 = 0
    fibo2 = 1

    print(fibo1, fibo2, sep='\n')

    while fibo <= num - fibo1:
        fibo = fibo2 + fibo1
        fibo1, fibo2 = fibo2, fibo
        print(fibo)

# Q7
# Write a function to generate and print factorial numbers up to n (provided by user).


def exercise_7():
    num = int(input("Enter an integer - "))  # type: int

    for n in range(1, num + 1):
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(f'Factorial of {n} is {result}')

# Q8
# Write a program using a for loop, that calculates exponentials.
# Your program should ask for base and exp. value form user. Note: Do not use ** operator and math module.


def exercise_8():
    base, exp = map(int, input("Enter base and exp (separated by space) - ").split(' '))
    result = 1
    for e in range(exp, 0, -1):
        result *= base

    print(result)

# Q9
# Write a program using loop that asks the user to enter an even number.
# If the number entered is not even then display an appropriate message and ask them to enter a number again.
# Do not stop until an even number is entered. Print a Congratulatory message at end.


def exercise_9():
    condition = True
    while condition:
        num = int(input("Enter an even number - "))

        if num % 2 == 1:
            print('Entered number is not an even number, try again')

        else:
            print('Contratulation!')
            condition = False

# Q10
# Using random module, Simulate tossing a coin N times. Hint: you can use zero for head and 1 for tails.


def exercise_10():
    import random
    # return random.choice([1, 0])
    return random.choice(['Head', 'Tail'])
