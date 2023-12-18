#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    g = 0
    printt = 0
    for g in range(0, x):
        try:
            print("{}".format(my_list[g]), end="")
            printt += 1
        except:
            continue
    print()
    return printt
