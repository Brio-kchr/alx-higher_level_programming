#!/usr/bin/python3
"""Used to execute some files if the code was run
directly and not imported"""
if __name__ == "__main__":
    import sys
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    print(result)
