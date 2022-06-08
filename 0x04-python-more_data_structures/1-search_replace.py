#!/usr/bin/python3
# 1-search_replace.py


def search_replace(my_list, search, replace):
    """Replacing occurrences of an element by another using a new list."""
    lst = my_list[:]
    for x in range(len(lst_list)):
        if lst[x] == search:
            lst[x] = replace
    return (lst)
