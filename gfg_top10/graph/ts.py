import unittest

from programming.gfg_top10.graph.Graph import Graph


def get_ts(g):
    visited = {v: False for v in g.vertex_set}
    result = []

    def get_ts_util(g, v, visited, result):
        if visited[v] != True:
            visited[v] = True
            adj_list = g.graph[v]
            for adj_v in adj_list:
                get_ts_util(g, adj_v, visited, result)
            result.append(v)

    for v in g.vertex_set:
        get_ts_util(g, v, visited, result)
    print(result)


# def get_ts(g):
#     visited = {v: False for v in g.vertex_set}
#     result = []
#     for v in g.vertex_set:
#         get_ts_util(g, v, visited, result)
#     print(result)
#
#
# def get_ts_util(g, v, visited, result):
#     if visited[v] != True:
#         visited[v] = True
#         adj_list = g.graph[v]
#         for adj_v in adj_list:
#             get_ts_util(g, adj_v, visited, result)
#         result.append(v)


class MyTestCase(unittest.TestCase):
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
        expected = "[0, 1, 3, 2, 4, 5]"
        actual = "[0, 1, 3, 2, 4, 5]"


if __name__ == '__main__':
    unittest.main()
