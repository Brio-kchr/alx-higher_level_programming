#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        res = 0 
        for i in range(0, x):
            print(my_list[i], end="")
            res += 1
        print()
    except IndexError:
        print()
    return res
