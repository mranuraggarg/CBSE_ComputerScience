# In analogy to the example, write a script that asks users for the temperature in F
# and prints the temperature in C. (Conversion: Celsius = (F - 32) * 5/9).


def f_convert_c():
    temp_f = float(input("Enter the temperature in F - "))
    temp_c = (temp_f - 32) * 5/9
    print('{0:0.3} deg C'.format(temp_c))
    return None

if __name__ == "__main__":
    f_convert_c()