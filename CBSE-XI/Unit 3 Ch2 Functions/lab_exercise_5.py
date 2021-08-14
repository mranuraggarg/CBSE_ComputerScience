# Write a Python function, odd, that takes in one number and returns True when the number is odd and
# False otherwise. You should use the % (mod) operator, not if.

def odd(num: int):
    assert isinstance(num, int)

    return num % 2 == 1

if __name__ == "__main__":
    # Print False
    print(odd(20))

    # Print True
    print(odd(21))