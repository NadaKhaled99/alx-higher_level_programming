#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    g = 0
    printt = 0
    for g in range(0, x):
        try:
            print("{:d}".format(my_list[g]), end="")
            printt += 1
        except (ValueError, TypeError):
            continue
    print()
    return printt
