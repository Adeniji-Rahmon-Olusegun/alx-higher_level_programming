#!/usr/bin/python3

for lcqe in range(ord('a') , (ord('z') + 1)):
    if ((chr(lcqe) != 'e') and (chr(lcqe) != 'q')):
        print("{0}".format(chr(lcqe)), end="")
