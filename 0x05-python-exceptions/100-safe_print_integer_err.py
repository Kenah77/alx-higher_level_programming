#!/usr/bin/python3
# 100-safe_print_integer_err.py


import sys


def safe_print_integer_err(val):
    """
    when valueError msg is caught, msg is passed
    to stderr
    Args:
        val (int): int to be printed
    Returns:
        If typeError or valueError occurs -> False.
        Else -> True.
    """
    try:
        print("{:d}".format(val))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
