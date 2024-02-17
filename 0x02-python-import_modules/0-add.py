#!/usr/bin/python3
"""Used to execute some files if the code was run
directly and not imported"""
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
