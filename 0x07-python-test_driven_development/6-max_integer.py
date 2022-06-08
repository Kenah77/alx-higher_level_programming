#!/usr/bin/python3


def max_integer(list=[]):
    if len(list) == 0:
        return None
    total = list[0]
    for x in list:
        if x > total:
            total = x
    return total
