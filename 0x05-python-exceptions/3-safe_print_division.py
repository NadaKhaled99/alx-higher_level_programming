#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        relt = a / b
    except:
        relt = None
    finally:
        print("Inside result: {}".format(relt))
    return relt
