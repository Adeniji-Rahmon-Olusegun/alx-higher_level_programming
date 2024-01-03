#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number."""

    if (number < 0):
        number = -(number)

    last_digit = (number % 10)

    print("{}".format(last_digit))

    return (last_digit)
