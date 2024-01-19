#!/usr/bin/python3
for i in range(8):
    for x in range(i, 10):
        if x == i:
            continue
        print("{:d}{:d}".format(i, x), end=", ")
print("{:d}{:d}".format(i + 1, x))
