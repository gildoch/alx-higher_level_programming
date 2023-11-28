#!/usr/bin/python3
for i in range(10):
    for x in range(10):
        if (i != x) and (i < x):
            print("{}{}".format(i, x), end="")
            if i + x != 17:
                print(", ", end="")
print()
