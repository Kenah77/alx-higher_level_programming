#!/usr/bin/python3
"""text_indentation
"""


def text_indentation(text):
    """Prints indentations for str
    """
    symbol = ['.', '?', ':']
    if type(text) != str:
        raise TypeError("text must of str")
    for x in text:
        print(x, end='')
        if x in symbol:
            print('\n\n', end='')
