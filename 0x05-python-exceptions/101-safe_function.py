#!/usr/bin/python3
# 101-safe_function.py


import sys


def safe_function(fct, *args):
    """execute func
    Args:
        fct: func to exec.
        args: fcr args.
    Returns:
        If error  -> None.
        Else -> the output of the call to fct.
    """
    try:
        output = fct(*args)
        return (output)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
