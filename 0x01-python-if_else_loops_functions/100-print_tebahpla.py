#!/usr/bin/python3

for rv in range(ord('z'), (ord('a') - 1), -1):
    print("{}".format(chr(rv - 32) if (rv % 2 != 0) else chr(rv)), end="")
