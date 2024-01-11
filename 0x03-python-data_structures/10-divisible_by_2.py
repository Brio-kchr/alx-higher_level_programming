#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    for x in range(len(my_list) - 1):
        if (my_list[x] % 2) == 0:
            new_list[x] = True
        else:
            new_list[x] = False
    return new_list
