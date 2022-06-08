#!/usr/bin/python3
# 2-uniq_add.py


def uniq_add(my_list=[]):
    """adding unique int ele of a lst"""
    sum = 0
    for i in set(my_list):
        sum += i
    return (sum)
