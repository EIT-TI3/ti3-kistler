#!/usr/bin/env python3
# (c) 2021 Martin Kistler

class Node:
    __id = 0

    def __init__(self, name_=None):
        self.inc_id()
        if name_ is None:
            self._name = 'Knoten ' + str(self.__id)
        else:
            self._name = name_
        self._next = []

        self.pre = None
        self.dist = float('inf')

    def __str__(self):
        output = self.name
        spacing = ''
        if not self._next:
            output += ' <end>\n'
        else:
            for edge in self._next:
                output += spacing + ' --' + str(edge) + '--> ' + edge.get_connect().name + '\n'
                spacing = ' ' * len(self.name)
        return output[:-1]

    def __gt__(self, other):
        return self.dist > other.dist

    def __lt__(self, other):
        return self.dist < other.dist

    def connect(self, e):
        self._next.append(e)

    def get_connects(self):
        return tuple(self._next)

    @classmethod
    def inc_id(cls):
        cls.__id += 1
        pass

    @property
    def name(self):
        return self._name

    def reset(self):
        self.pre = None
        self.dist = float('inf')

    def neighbours(self):
        for edge in self.get_connects():
            yield edge.get_connect(), edge.weight
