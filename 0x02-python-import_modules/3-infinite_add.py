#!/usr/bin/python3

import sys

if __name__ == "__main__":

    sums = 0

    if (len(sys.argv) == 1):
        print("{}".format(sums))
    else:
        for arg in range(1, len(sys.argv)):
            sums += int(sys.argv[arg])
        print("{}".format(sums))
