#!/usr/bin/python3

for p_1 in range(10):
    for p_2 in range(p_1+1, 10):
        if (p_1 != p_2 and p_1 < 8):
            print("{:d}{:d},".format(p_1, p_2), end=" ")
        else:
            print("{:d}{:d}".format(p_1, p_2))
