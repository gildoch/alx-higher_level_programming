#!/usr/bin/python3

def read_file(filename=""):
    """ Reads a text file"""
    with open(filename, mode="r", encoding="UTF-8") as file:
        print(file.read())
