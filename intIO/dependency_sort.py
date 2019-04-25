"""
install dependencies before installing packages
idea : topological sort
comp : same as dfs = O(V+E)
"""
from gfg_top10.graph.Graph import Graph


def package_dependencies(g):
    if not g:
        return -1
    res, visited, visiting = [], set(), set()

    def dfs(v):
        if v in visited:
            return
        visiting.add(v)
        for adj_v in g.graph[v]:
            if adj_v in visiting:
                raise Exception("have cycle in dependencies")
            if adj_v not in visited:
                dfs(adj_v)
        visiting.remove(v)
        visited.add(v)
        res.append(v)

    for v in g.vertex_set:
        dfs(v)
    return res


g = Graph()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
package_dependencies(g)
expected = [0, 1, 3, 2, 4, 5]
actual = [0, 1, 3, 2, 4, 5]
print(expected == actual)

g = Graph()
g.add_edge(0, 1)
package_dependencies(g)
expected = [0, 1]
actual = [0, 1]
print(expected == actual)

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 0)
package_dependencies(g)
expected = [0, 1]
actual = [0, 1]
print(expected == actual)
