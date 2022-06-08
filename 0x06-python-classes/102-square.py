#!/usr/bin/python3
# 102-square.py


class Square:
    """rep square"""
    def __init__(self, size=0):
        """
        size : sze
        """
        self.__size = size

    @property
    def size(self):
        """
        get private instance attr
        """
        return self.__size

    @size.setter
    def size(self, val):
        """
        set instance attr
        """
        self.__size = val
        try:
            assert type(val) == int
        except:
            raise TypeError("size must be of int")
        if val < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """return area"""
        area = self.__size ** 2
        return area

    def __lt__(self, tmp):
        """check <"""
        if self.__size ** 2 < tmp.__size ** 2:
            return True
        return False

    def __le__(self, tmp):
        """check <="""
        if self.__size ** 2 <= tmp.__size ** 2:
            return True
        return False

    def __eq__(self, tmp):
        """check for =="""
        if self.__size ** 2 == tmp.__size ** 2:
            return True
        return False

    def __ne__(self, tmp):
        """check for !="""
        if self.__size ** 2 != tmp.__size ** 2:
            return True
        return False

    def __gt__(self, tmp):
        """check for >"""
        if self.__size ** 2 > tmp.__size ** 2:
            return True
        return False

    def __ge__(self, tmp):
        """check for >="""
        if self.__size ** 2 >= tmp.__size ** 2:
            return True
        return False
