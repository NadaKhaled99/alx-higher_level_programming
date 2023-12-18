#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        t = fct(*args)
        return t
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
