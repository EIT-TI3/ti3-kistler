#!/usr/bin/env python3
# (c) 2021 Martin Kistler

class Node:
    id = 1

    def __init__(self, name_=None):
        if name_ is None:
            self._name = 'Knoten ' + str(self.id)
        else:
            self._name = name_
        self.inc_id()
        self._next = []

    def __str__(self):
        output = self.name
        try:
            output += ' ---> ' + self._next[0].name + '\n'
        except IndexError:
            output += ' <end>'

        for node in self._next[1:]:
            output += ' '*len(self.name) + ' ---> ' + node.name

        return output

    def connect(self, n):
        self._next.append(n)

    def get_connects(self):
        return tuple(self._next)

    @classmethod
    def inc_id(cls):
        cls.id += 1

    @property
    def name(self):
        return self._name
