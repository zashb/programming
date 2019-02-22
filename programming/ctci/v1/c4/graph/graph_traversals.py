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
    print(v, end=",")
    for i in g.graph[v]:
        if not visited[v]:
            dfs_util(i, visited, g)


def bfs(g, u):
    """queue is edited while looping over it"""
    visited = [False] * g.numvertices
    queue = [u]
    visited[u] = True
    # ideally queue[:]
    while queue:
        u = queue.pop(0)
        print(u, end=",")
        for i in g.graph[u]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def recursive_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=",")
    for v in graph[start]:
        if v not in visited:
            recursive_dfs(graph, v, visited)


# def recursive_topological_sort(graph, start, visited=None, stack=[]):
#     # TODO : figure this out!!!
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start, end=",")
#     for v in graph[start]:
#         if v not in visited:
#             recursive_topological_sort(graph, v, visited)
#     stack.insert(0, start)
#     return stack


class Test(unittest.TestCase):
    """if alphabet nodes are used, used ord()"""
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

    def test_rdfs(self):
        print(recursive_dfs(self.g.graph, 0))

    def test_rts(self):
        g = Graph(6)
        g.add_edge(5, 2)
        g.add_edge(5, 0)
        g.add_edge(4, 0)
        g.add_edge(4, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        print(recursive_topological_sort(g.graph, 5))


if __name__ == "__main__":
    unittest.main()
