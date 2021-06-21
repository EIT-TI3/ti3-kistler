#!/usr/bin/env python3
# (c) 2021 Martin Kistler


class Node:
    __id = 0

    def __init__(self, name_=None):
        Node.__id += 1
        if name_ is None:
            self.__name = 'Knoten ' + str(self.__id)
        else:
            self.__name = name_
        self.__next = []

        self.pre = None
        self.dist = float('inf')

    @property
    def name(self):
        return self.__name

    def connect(self, e):
        self.__next.append(e)

    def get_connects(self):
        return tuple(self.__next)

    def __str__(self):
        output = self.name
        spacing = ''
        if not self.__next:
            output += ' <end>\n'
        else:
            for edge in self.__next:
                output += spacing + ' --' + str(edge) + '--> ' + edge.get_connect().name + '\n'
                spacing = ' ' * len(self.name)
        return output[:-1]

    def __gt__(self, other):
        return self.dist > other.dist

    def __lt__(self, other):
        return self.dist < other.dist

    def reset(self):
        self.pre = None
        self.dist = float('inf')

    def neighbours(self):
        for edge in self.get_connects():
            yield edge.get_connect(), edge.weight
