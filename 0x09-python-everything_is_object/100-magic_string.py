#!/usr/bin/python3
def magic_string(cnt=[0]):
    cnt[0] += 1
    return str("BestSchool, " * cnt[0])[:-2]
