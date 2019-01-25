import unittest
from collections import defaultdict


class Graph:
    def __init__(self, vc):
        self.vc = vc
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


def get_topological_sort(g):
    visited = [False] * g.vc
    stack = []
    for i in range(g.vc):
        if not visited[i]:
            topological_sort_util(g, i, visited, stack)
    print(stack)


def topological_sort_util(g, v, visited, stack):
    visited[v] = True
    for i in g.graph[v]:
        if not visited[i]:
            topological_sort_util(g, i, visited, stack)
    stack.insert(0, v)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        g = Graph(6)
        g.add_edge(5, 2)
        g.add_edge(5, 0)
        g.add_edge(4, 0)
        g.add_edge(4, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        get_topological_sort(g)

    def test_build_order(self):
        g = Graph(6)
        g.add_edge(0, 3)
        g.add_edge(5, 1)
        g.add_edge(1, 3)
        g.add_edge(5, 0)
        g.add_edge(3, 2)
        get_topological_sort(g)


if __name__ == '__main__':
    unittest.main()
