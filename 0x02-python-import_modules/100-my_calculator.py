#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    len_arg = len(argv) - 1

    if (len_arg != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        num_1 = int(argv[1])
        operator = argv[2]
        num_2 = int(argv[3])

        if (operator == "+"):
            result = add(num_1, num_2)
            print("{:d} + {:d} = {:d}".format(num_1, num_2, result))
            exit(0)
        elif (operator == "-"):
            result = sub(num_1, num_2)
            print("{:d} - {:d} = {:d}".format(num_1, num_2, result))
            exit(0)
        elif (operator == "*"):
            result = mul(num_1, num_2)
            print("{:d} * {:d} = {:d}".format(num_1, num_2, result))
            exit(0)
        elif (operator == "/"):
            result = div(num_1, num_2)
            print("{:d} / {:d} = {:d}".format(num_1, num_2, result))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)