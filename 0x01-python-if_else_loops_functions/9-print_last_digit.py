#!/usr/bin/python3
def print_last_digit(number):
    lst_dig = int(repr(number)[-1])
    print("{}".format(lst_dig), end="")
    return lst_dig
