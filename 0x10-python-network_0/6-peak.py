#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted intergers
    """
    if len(list_of_integers) < 1:
        return (None)

    start, end=0, len(list_of_integers) - 1
    
    lst = list_of_integers
    while (start < end):
        mid = start + (end - start) // 2

        #Check if mid is a peak
        if lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return lst[mid]

        if lst[mid-1] > lst[mid + 1]:
            end = mid
        else:
            start=mid + 1
    return lst[start]
