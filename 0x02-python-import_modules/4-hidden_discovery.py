#!/usr/bin/python3
"""Used to execute some files if the code was run
directly and not imported"""
if __name__ == "__main__":
    import hidden_4
    file1 = dir(hidden_4)
    for i in range(0, len(file1)):
        if file1[i][0:2] != "__":
            print(file1[i])
