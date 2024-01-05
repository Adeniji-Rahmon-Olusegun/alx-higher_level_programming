#!/usr/bin/python3

import sys

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    ag = sys.argv
    operator_list = ["+", "-", "*", "/"]

    if len(ag) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        if ag[2] not in operator_list:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        elif ag[2] == "+":
            print(f"{ag[1]} + {ag[3]} = {add(int(ag[1]), int(ag[3]))}")
        elif ag[2] == "-":
            print(f"{ag[1]} - {ag[3]} = {sub(int(ag[1]), int(ag[3]))}")
        elif ag[2] == "*":
            print(f"{ag[1]} * {ag[3]} = {mul(int(ag[1]), int(ag[3]))}")
        elif ag[2] == "/":
            print(f"{ag[1]} / {ag[3]} = {div(int(ag[1]), int(ag[3]))}")
