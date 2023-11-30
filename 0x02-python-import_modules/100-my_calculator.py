#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        opr = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if opr == "+":
            print("{} {} {} = {}".format(a, opr, b, add(a, b)))
        elif opr == "-":
            print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
        elif opr == "*":
            print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
        elif opr == "/":
            print("{} {} {} = {}".format(a, opr, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
