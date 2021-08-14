# Q1
# Input a string “Green Revolution”. Write a script to print the string in reverse.


def exercise_1():
    string = "Green Revolution"
    return string[::-1]

# Q2
# Input the string “Success”. Write a script of check if the string is a palindrome or not


def exercise_2():
    string = "Success"
    return string.lower() == string[::-1].lower()

# Q3
# Input the string “Successor”. Write a script to split the string at every occurrence of the letter s.


def exercise_3():
    string = "Successor"
    return string.lower().count('s')

# Q4
# Input the string “Successor”. Write a script to partition the string at the occurrence of the letter s.
# Also Explain the difference between the function split( ) and partition().


def exercise_4():
    string = "Successor"
    return string.lower().split('s')

# Q5
# Write a program to print the pyramid.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


def exercise_5():
    for i in range(1, 6):
        print((str(i) + ' ')*i)

# Q10
# Write a program to print alternate characters in a string. Input a string of your own choice.


def exercise_6(string: str):
    return string[::2]

# Q11
# Input a string „Python‟. Write a program to print all the letters except the letter‟y‟.


def exercise_11():
    string = "Python"
    return str.replace(string, 'y', '')

# Q12
# Consider the string str=”Global Warming”
# Write statements in python to implement the following
# a) To display the last four characters.
# b) To display the substring starting from index 4 and ending at index 8.
# c) To check whether string has alphanumeric characters or not.
# d) To trim the last four characters from the string.
# e) To trim the first four characters from the string.
# f) To display the starting index for the substring „Wa‟.
# g) To change the case of the given string.
# h) To check if the string is in title case.
# i) To replace all the occurrences of letter „a‟ in the string with „*‟

def exercise_12():
    string = "Global Warming"

    # a
    print(string[-4:])

    # b
    print(string[4:9])

    # c
    print(any(ch.isalnum for ch in string))

    # d
    print(string[:-4])

    # e
    print(string[5:])

    # f
    print(string.find('Wa'))

    # g
    print(string.lower())

    # h
    print(string.istitle())

    # i
    print(string.replace('a', '*'))

exercise_12()