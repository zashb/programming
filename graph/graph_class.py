from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertex_set = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.vertex_set.add(u)
        self.vertex_set.add(v)
