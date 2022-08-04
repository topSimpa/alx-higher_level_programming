#!/usr/bin/python3
""" defines a singly linked list"""


class Node:
    """ The defines the Node of the singly linked list """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return(self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return(self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if type(value) not in [Node, type(None)]:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This defines the singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """ insert a node in a singly_list """
        if (self.__head is None):
            self.__head = Node(value)
        else:
            r = self.__head
            new = Node(value)
            while r.next_node is not None:
                if value >= r.data and value <= (r.next_node).data:
                    break
                r = r.next_node
            if new.data < (self.__head).data:
                new.next_node = self.__head
                self.__head = new
            else:
                new.next_node = r.next_node
                r.next_node = new

    def __str__(self):
        """ This is the method to print with"""
        r = self.__head

        rep = f"{r.data}"
        r = r.next_node
        while r is not None:
            rep += f"\n{r.data}"
            r = r.next_node
        return(rep)
