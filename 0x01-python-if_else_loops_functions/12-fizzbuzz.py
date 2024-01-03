#!/usr/bin/python3

def fizzbuzz():
    """Prints 1 to 100 in the FizzBuzz style"""

    for fizzbuzz in range(1, 101):
        if ((fizzbuzz % 3 == 0) and (fizzbuzz % 5 == 0)):
            print("FizzBuzz", end=" ")
        elif (fizzbuzz % 3 == 0):
            print("Fizz", end=" ")
        elif (fizzbuzz % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(fizzbuzz, end=" ")
