#!/usr/bin/python3

""" Node class"""


class Node:
    """ the base node for linked list"""

    def __init__(self, data, next_node=None):
        """ constructor for node class
        Args:
            data: value stored in node class
            next_node: pointer to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter, gets the value of stored in the instance node
        """
        return self.__data

    @data.setter
    def data(self, vlaue):
        """ sets the data to value """
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ gets the value the next poits to """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the value the next poits to """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ a singly linked list class """
    def __init__(self):
        """ constructor to initialize linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ inserts node to linked list inserted manner
        Args:
            value: data to be inserted in
        """
        n = Node(value)

        if self.__head is None:
            n.next_node = None
            self.__head = n
        elif self.__head.data > value:
            n.next_node = self.__head
            self.__head = n
        else:
            t = self.__head
            while (t.next_node is not None and t.next_node.data < value):
                t = t.next_node

            n.next_node = t.next_node
            t.next_node = n

    def __str__(self):
        """ prints values of linked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
