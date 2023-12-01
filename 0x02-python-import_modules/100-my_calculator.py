#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    a = int(argv[1])
    b = int(argv[3])
    functions = ["+", "-", "*", "/"]

    from calculator_1 import add, sub, mul, div
    operations = [add, sub, mul, div]
    for h, g in enumerate(functions):
        if argv[2] == g:
            print("{} {} {} = {}".format(a, g, b, operations[h](a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
