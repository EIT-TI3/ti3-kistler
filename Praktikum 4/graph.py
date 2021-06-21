#!/usr/bin/env python3
# (c) 2021 Martin Kistler

from node import Node
from edge import Edge


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def __str__(self):
        output = 'Knoten:\n-------\n'
        for node in self.nodes:
            output += str(node) + '\n'

        output += '\nKanten:\n-------\n'
        for edge in self.edges:
            output += str(edge) + '\n'

        return output

    def new_node(self, name=None):
        node = Node(name)
        self.nodes.append(node)
        return node

    def new_edge(self, name, weight):
        edge = Edge(name, weight)
        self.edges.append(edge)
        return edge

    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

    def find_edge(self, name):
        for edge in self.edges:
            if edge.name == name:
                return edge

    def path_length(self, path_node_names):
        length = 0
        nodes = list(map(self.find_node, path_node_names))

        for node, next_node in zip(nodes, nodes[1:]):
            for neighbour_node, weight in node.neighbours():
                if neighbour_node == next_node:
                    length += weight
                    break
            else:
                length = -1
                break

        return length

    def find_path(self, start, target):
        start_node = self.find_node(start)
        target_node = self.find_node(target)

        unvisited_nodes = self.nodes.copy()
        for node in unvisited_nodes:
            node.reset()
        start_node.dist = 0

        path = [start_node]

        while unvisited_nodes:
            visiting_node = min(unvisited_nodes)
            if visiting_node == target_node:
                break
            unvisited_nodes.remove(visiting_node)
            path.append(visiting_node)

            for node, weight in visiting_node.neighbours():
                dist_to_node = visiting_node.dist + weight
                if dist_to_node < node.dist:
                    node.dist = dist_to_node
                    node.pre = visiting_node

        return [node.name for node in path], target_node.dist
