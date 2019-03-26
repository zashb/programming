import unittest
from collections import deque

from programming.gfg_top10.graph.Graph import Graph


def get_bfs(g, start):
    visited = {v: False for v in g.vertex_set}
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        if visited[v] != True:
            visited[v] = True
            print(v, end=" ")
            adj_list = g.graph[v]
            for adj_v in adj_list:
                queue.append(adj_v)


class MyTestCase(unittest.TestCase):
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
        expected = "2 0 3 1"
        actual = "2 0 3 1"


if __name__ == '__main__':
    unittest.main()
