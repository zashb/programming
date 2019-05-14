# ignores cycle

from graph.graph_class import Graph


def dfs(edges):
    if not edges:
        return None

    graph = Graph()
    res = []

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    visited = {v: False for v in graph.vertex_set}

    def dfs_util(graph, v, visited, res):
        if not visited[v]:
            visited[v] = True
            res.append(v)
            for adj_v in graph.graph[v]:
                dfs_util(graph, adj_v, visited, res)

    for v in graph.vertex_set:
        dfs_util(graph, v, visited, res)

    return res


expected = ["a", "b", "c", "d"]
actual = dfs([["a", "b"], ["a", "c"], ["b", "c"], ["c", "a"], ["c", "d"], ["d", "d"]])
print(expected == actual)
