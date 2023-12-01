#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    tuple_str = ()

    if str_len == 0:
        tuple_str = (str_len, "None")
    else:
        tuple_str = (str_len, sentence[0])

    return tuple_str
