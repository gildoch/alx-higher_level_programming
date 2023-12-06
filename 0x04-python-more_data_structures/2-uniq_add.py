#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    for elem in my_list:
        if elem not in unique_list:
            unique_list.append(elem)
    soma = 0
    for i in unique_list:
        soma += i
    return soma
