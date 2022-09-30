#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_tup = set(my_list)
    sum = 0
    for s in new_tup:
        sum += s

    return sum
