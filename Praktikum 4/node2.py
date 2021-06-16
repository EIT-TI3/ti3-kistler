#!/usr/bin/env python3
# (c) 2021 Martin Kistler

class Node:
    id = 0

    def __init__(self, name_):
        self._name = name_
        self.next = []

    def __str__(self):
        output = self.name
        try:
            output += ' ---> ' + self.next[0].name + '\n'
        except IndexError:
            output += ' <end>'

        for node in self.next[1:]:
            output += ' '*len(self.name) + ' ---> ' + node.name

        return output

    @property
    def name(self):
        return self._name
