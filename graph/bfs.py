from collections import deque

from graph.graph_class import Graph


def bfs(edges, s):
    if not edges and not s:
        return None

    graph = Graph()
    queue = deque()
    queue.append(s)
    res = []

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    visited = {v: False for v in graph.vertex_set}

    while queue:
        v = queue.popleft()
        if not visited[v]:
            visited[v] = True
            res.append(v)
            for adj_v in graph.graph[v]:
                queue.append(adj_v)
    return res


expected = [2, 0, 3, 1]
actual = bfs([[0, 1], [0, 2], [1, 2], [2, 0], [2, 3], [3, 3]], 2)
print(expected == actual)
