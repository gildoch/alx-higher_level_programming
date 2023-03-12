#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    summ = 0
    if argc == 1:
        print(summ)
    elif argc > 1:
        for i in range(1, argc):
            summ += int(argv[i])
        print(summ)
