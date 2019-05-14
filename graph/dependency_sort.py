"""
install dependencies before installing packages
idea : topological sort
comp : same as dfs = O(V+E)
"""
from graph.graph_class import Graph


def package_dependencies(dependencies):
    if not dependencies:
        return -1

    graph = Graph()
    res, visited, visiting = [], set(), set()

    for i in dependencies:
        graph.add_edge(i[0], i[1])

    def dfs(v):
        if v in visited:
            return
        visiting.add(v)
        for adj_v in graph.graph[v]:
            if adj_v in visiting:
                raise Exception("cycle in dependencies")
            if adj_v not in visited:
                dfs(adj_v)
        visiting.remove(v)
        visited.add(v)
        res.append(v)

    for v in graph.vertex_set:
        dfs(v)

    return res


actual = package_dependencies([[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]])
expected = [0, 1, 3, 2, 4, 5]
print(expected == actual)

actual = package_dependencies([[0, 1]])
expected = [1, 0]
print(expected == actual)

actual = package_dependencies([[0, 1], [1, 0]])
expected = "exception "
print(expected == actual)
