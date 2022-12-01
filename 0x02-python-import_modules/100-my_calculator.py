#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    len_arg = len(argv) - 1

    if (len_arg != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])

        if (operator == "+"):
            result = add(a, b)
            print("{:d} + {:d} = {:d}".format(a, b, result))
            exit(0)
        elif (operator == "-"):
            result = sub(a, b)
            print("{:d} - {:d} = {:d}".format(a, b, result))
            exit(0)
        elif (operator == "*"):
            result = mul(a, b)
            print("{:d} * {:d} = {:d}".format(a, b, result))
            exit(0)
        elif (operator == "/"):
            result = div(a, b)
            print("{:d} / {:d} = {:d}".format(a, b, result))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
