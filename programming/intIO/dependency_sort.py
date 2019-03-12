"""
install dependencies before installing packages
idea : topological sort
comp : same as dfs = O(V+E)
"""
from programming.gfg_top10.graph.Graph import Graph


def topological_sort(g):
    visited = {v: False for v in g.vertex_set}
    res = []

    def ts_util(g, visited, v, res):
        if visited[v] == False:
            visited[v] = True
            adj_list = g.graph[v]
            for adj_v in adj_list:
                ts_util(g, visited, adj_v, res)
            res.append(v)

    for v in g.vertex_set:
        ts_util(g, visited, v, res)
    return res


g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
topological_sort(g)
expected = [0, 1, 3, 2, 4, 5]
actual = [0, 1, 3, 2, 4, 5]
print(expected == actual)
