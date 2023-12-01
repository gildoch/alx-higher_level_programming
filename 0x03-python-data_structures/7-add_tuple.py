#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lena = len(tuple_a)
    lenb = len(tuple_b)
    sum_t = ()

    if lena == 0:
        tuple_a = (0, 0)
    if lenb == 0:
        tuple_b = (0, 0)
    if lena == 1:
        if tuple_a[0]:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, tuple_a[1])
    if lenb == 1:
        if tuple_b[0]:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, tuple_b[1])
    if lena > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if lenb > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    sum_t = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_t
