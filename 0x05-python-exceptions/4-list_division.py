#!/usr/bin/python3
# 4-list_division.py


def list_division(my_list_1, my_list_2, list_length):
    """Divides 2 lst ele by ele"""
    lst = []
    for x in range(0, list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("Invalid type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            lst.append(result)
    return (lst)
