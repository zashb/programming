import unittest
from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex_set = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertex_set.add(u)
        self.vertex_set.add(v)


def get_dfs(g):
    visited = {v: False for v in g.vertex_set}
    for v in g.vertex_set:
        dfs_util(g, v, visited)


def dfs_util(g, v, visited):
    if not visited[v]:
        visited[v] = True
        print(v, end=",")
        adj_list = g.graph[v]
        for adj_v in adj_list:
            dfs_util(g, adj_v, visited)


def get_ts(g):
    visited = {v: False for v in g.vertex_set}
    result = []
    for v in g.vertex_set:
        ts_util(g, v, visited, result)
    print(result)


def ts_util(g, v, visited, result):
    if not visited[v]:
        visited[v] = True
        # print(v, end=",")
        adj_list = g.graph[v]
        for adj_v in adj_list:
            ts_util(g, adj_v, visited, result)
        result.append(v)


def get_bfs(g, start):
    visited = {v: False for v in g.vertex_set}
    visited[start] = True
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        print(v, end=",")
        adj_list = g.graph[v]
        for adj_v in adj_list:
            if not visited[adj_v]:
                visited[adj_v] = True
                queue.append(adj_v)


class Test(unittest.TestCase):
    def test_dfs(self):
        g = Graph()
        g.add_edge("a", "b")
        g.add_edge("a", "c")
        g.add_edge("b", "c")
        g.add_edge("c", "a")
        g.add_edge("c", "d")
        g.add_edge("d", "d")
        print("\n dfs : ")
        get_dfs(g)

    def test_bfs(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)
        print("\n bfs : ")
        get_bfs(g, 2)

    def test_ts(self):
        g = Graph()
        g.add_edge(5, 2)
        g.add_edge(5, 0)
        g.add_edge(4, 0)
        g.add_edge(4, 1)
        g.add_edge(2, 3)
        g.add_edge(3, 1)
        print("\n ts : ")
        get_ts(g)
