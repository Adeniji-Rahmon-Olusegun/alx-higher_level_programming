#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sums = 0

    if (len(sys.argv) == 1):
        print("{}".format(0))
    elif(len(sys.argv) == 2):
        print("{}".format(int(sys.argv[1]) + 0))
    elif (len(sys.argv) > 2):
        for arg in range(1, len(sys.argv)):
            sums += int(sys.argv[arg])
        print("{}".format(sums))
