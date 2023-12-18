#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    g = 0
    n_list = []
    relt = 0
    for g in range(0, list_length):
        try:
            relt = (my_list_1[g] / my_list_2[g])
        except TypeError:
            relt = 0
            print("wrong type")
        except ZeroDivisionError:
            relt = 0
            print("division by 0")
        except IndexError:
            relt = 0
            print("out of range")
        finally:
            n_list.append(relt)
    return n_list
