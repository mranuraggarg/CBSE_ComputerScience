# Write a Python function, fourthPower( ), that takes in one number and returns that value raised to the fourth power.


def fourthPower(num: int):
    return round(num ** 4, 2)


if __name__ == "__main__":
    # Print 16
    print(fourthPower(2))

    # Print 23.43
    print(fourthPower(2.2))

    # Print 16
    print(fourthPower(-2))