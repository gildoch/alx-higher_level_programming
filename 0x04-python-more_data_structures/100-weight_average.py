#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    tmp_mult = 0
    tmp_add = 0

    for t in my_list:
        tmp_mult += t[0] * t[1]
        tmp_add += t[1]
    return (tmp_mult / tmp_add)
