#!/usr/bin/python3

def remove_char_at(str, n):
    """romoves a character at a particular index position."""

    if (n >= 0 and n < len(str)):
        return str[:n] + str[n+1:]
    return str
