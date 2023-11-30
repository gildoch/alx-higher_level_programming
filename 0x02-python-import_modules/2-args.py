#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("{} argument:".format(argc - 1))
        print("{}: {}".format(argc - 1, argv[1]))
    elif argc > 2:
        print("{} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{}: {}".format(i, argv[i]))
