import unittest

from programming.gfg_top10.graph.Graph import Graph


def get_dfs(g):
    visited = {v: False for v in g.vertex_set}
    for v in g.vertex_set:
        dfs_util(g, v, visited)


def dfs_util(g, v, visited):
    if visited[v] != True:
        visited[v] = True
        print(v, end=" ")
        adj_list = g.graph[v]
        for adj_v in adj_list:
            dfs_util(g, adj_v, visited)


class MyTestCase(unittest.TestCase):
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
        expected = "a b c d"
        actual = "a b c d"


if __name__ == '__main__':
    unittest.main()
