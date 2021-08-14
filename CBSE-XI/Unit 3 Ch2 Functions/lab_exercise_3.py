# Write a script that asks a user for a number. Then adds 3 to that number,
# and then multiplies the result by 2, subtracts twice the original number, then prints the result.

def add_3():
    num = float(input("Enter a number - "))
    result = 2 * (num + 3) - (2 * num)
    print(result)
    return None

if __name__ == "__main__":
    add_3()