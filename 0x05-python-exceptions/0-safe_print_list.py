#!/usr/bin/python3
# 0-safe_print_list.py


def safe_print_list(my_list=[], x=0):
    """
    Args:
        my_list (list): lst
        x (int): num of eements to print
    """
    count = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
