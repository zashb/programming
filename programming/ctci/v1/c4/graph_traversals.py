import unittest
from collections import defaultdict


class Graph:
    def __init__(self, size):
        self.numvertices = size
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)


def dfs(g):
    visited = [False] * g.numvertices
    for i in range(g.numvertices):
        if not visited[i]:
            dfs_util(i, visited, g)


def dfs_util(v, visited, g):
    visited[v] = True
    print(v)
    for i in g.graph[v]:
        if not visited[v]:
            dfs_util(i, visited, g)


def bfs(g, u):
    visited = [False] * g.numvertices
    queue = [u]
    visited[u] = True
    while queue:
        u = queue.pop(0)
        print(u)
        for i in g.graph[u]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


class Test(unittest.TestCase):
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(4, 5)

    def test_dfs(self):
        print("testing dfs")
        dfs(self.g)

    def test_bfs(self):
        print("testing bfs")
        bfs(self.g, 2)


if __name__ == "__main__":
    unittest.main()
