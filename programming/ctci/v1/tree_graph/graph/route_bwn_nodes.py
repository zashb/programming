import unittest

from programming.ctci.v1.tree_graph.graph.graph_traversals import Graph


class Test(unittest.TestCase):
    """Given a directed graph, design an algorithm to find out whether there is a route between two nodes. """
    g = Graph()
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
    visited = {v: False for v in g.vertex_set}
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
