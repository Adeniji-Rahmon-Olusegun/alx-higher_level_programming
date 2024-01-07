#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and
    its first character

    Args:
        string: sentence

    Return:
            tuple: length of string and first character
            tuple: 0 if empty string and None for first character
    """

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
