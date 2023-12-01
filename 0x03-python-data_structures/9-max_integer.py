#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return None

    max_num = my_list[0]
    for elem in my_list:
        if elem > max_num:
            max_num = elem
    return max_num
