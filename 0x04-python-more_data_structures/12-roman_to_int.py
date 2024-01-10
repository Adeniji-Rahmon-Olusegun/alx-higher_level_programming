#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Converts roman numeral to integer

    Args:
        roman_string: str

    Return:
            integer
    """
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0

    converted_numeral = 0
    positional_check = 0

    rom_fig = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for pos in reversed(roman_string):
        roman_to_dec = rom_fig[pos]

        if roman_to_dec < positional_check:
            converted_numeral -= roman_to_dec
        else:
            converted_numeral += roman_to_dec
        positional_check = roman_to_dec

    return converted_numeral
