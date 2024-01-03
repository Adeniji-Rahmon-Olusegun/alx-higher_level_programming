#!/usr/bin/python3

def uppercase(str):
    """Prints characters in uppercase letters."""

    upper_letters = ""

    for letter in str:
        if (ord(letter) >= 97 and ord(letter) <= 122):
            upper_char = chr((ord(letter) - 32))
            upper_letters += upper_char
        else:
            upper_letters += letter
    print("{}".format(upper_letters))
