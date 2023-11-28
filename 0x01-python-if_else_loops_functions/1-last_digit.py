#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lst_dig = int(repr(number)[-1]) * -1
else:
    lst_dig = int(repr(number)[-1])

if lst_dig > 5:
    print(f"Last digit of {number} is {lst_dig} and is greater than 5")
elif lst_dig == 0:
    print("Last digit of {} is {} and is 0".format(number, lst_dig))
elif (lst_dig < 6) and (lst_dig != 0):
    print(f"Last digit of {number} is {lst_dig} and is less than 6 and not 0")
