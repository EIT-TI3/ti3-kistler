#!/usr/bin/env python3
# (c) 2021 Martin Kistler

class Edge:
    def __init__(self, name_, weight_):
        self.__name = name_
        self.weight = weight_
        self.__next = None

    def connect(self, n):
        self.__next = n

    def get_connect(self):
        return self.__next

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return self.name + '/' + str(self.weight)
