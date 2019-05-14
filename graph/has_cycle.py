"""
prob: has cycle
idea: dfs, rec_stack
comp:
"""
from graph.graph_class import Graph


def has_cycle(edges):
    if not edges:
        return False

    graph = Graph()

    for edge in edges:
        graph.add_edge(edge[0], edge[1])

    visited = {v: False for v in graph.vertex_set}
    rec_stack = {v: False for v in graph.vertex_set}

    def has_cycle_util(g, v, visited, rec_stack):
        if not visited[v]:
            visited[v] = True
            rec_stack[v] = True
            adj_list = g.graph[v]
            for adj_v in adj_list:
                if has_cycle_util(g, adj_v, visited, rec_stack):
                    return True
        elif rec_stack[v]:
            return True
        rec_stack[v] = False
        return False

    for v in graph.vertex_set:
        if has_cycle_util(graph, v, visited, rec_stack):
            return True
    return False


expected = True
actual = has_cycle([[1, 2], [2, 3], [3, 4], [3, 5], [3, 1]])
print(expected == actual)
