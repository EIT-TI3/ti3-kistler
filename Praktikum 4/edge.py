#!/usr/bin/env python3
# (c) 2021 Martin Kistler

class Edge:
    def __init__(self, name_, weight_):
        self._name = name_
        self.weight = weight_
        self._next = None

    def connect(self, n):
        self._next = n

    def get_connect(self):
        return self._next

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name + '/' + str(self.weight)
