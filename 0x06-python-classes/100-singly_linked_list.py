#!/usr/bin/python3
# 100-singly_linked_list.py
"""singly-linked list."""


class Node:
    """Represent node"""

    def __init__(self, data, next_node=None):
        """
            Args:
            data (int): data
            next_node (Node): ptr.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set data"""
        return (self.__data)

    @data.setter
    def data(self, val):
        if val != int(val):
            raise TypeError("data must be of int")
        self.__data = val

    @property
    def next_node(self):
        """Get/setnext_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, val):
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a node obj")
        self.__next_node = val


class SinglyLinkedList:
    """Rep singly-linked list."""

    def __init__(self):
        """Initializing...."""
        self.__head = None

    def sorted_insert(self, val):
        """
            Args:
            value (Node): new Node to enter.

        """
        new = Node(val)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > val:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < val):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """rep of a singly-linkedList."""
        val = []
        temp = self.__head
        while temp is not None:
            val.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(val))
