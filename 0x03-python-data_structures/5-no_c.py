#!/usr/bin/python3
def no_c(my_string):
    newstr = ""
    for car in my_string:
        if (car != "c") and (car != "C"):
            newstr += car
    return newstr
