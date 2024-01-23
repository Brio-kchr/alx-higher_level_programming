#!/usr/bin/python3
def uppercase(stir):
    for char in stir:
        case = ord(char)
        if (case > 96 && case < 123):
            case = ord(char) - 32
        print("{}".format(chr(case)))
    print()
