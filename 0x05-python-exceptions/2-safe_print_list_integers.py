#!/usr/bin/python3
# 2-safe_print_list_integers.py


def safe_print_list_integers(my_list=[], x=0):
    """print first x int elements of a lst """
    count = 0
    for j in range(0, x):
        try:
            print("{:d}".format(my_list[j]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
