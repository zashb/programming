import unittest
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


class Test(unittest.TestCase):
    """Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    def test_is_reachable(self):
        test_cases = [(1, 3), (3, 1)]
        for case in test_cases:
            actual = is_reachable(self.g, case[0], case[1])
            if actual:
                print("{} is reachable from {}".format(case[1], case[0]))
            else:
                print("{} is not reachable from {}".format(case[1], case[0]))


def is_reachable(g, s, d):
    visited = [False] * g.vertices
    queue = [s]
    visited[s] = True
    while queue:
        node = queue.pop(0)
        if node == d:
            return True
        for i in g.graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False


if __name__ == "__main__":
    unittest.main()
