"""
prob: has cycle
idea: dfs, rec_stack
comp:
"""
from gfg_top10.graph.Graph import Graph


def has_cycle(g):
    visited = {v: False for v in g.vertex_set}
    rec_stack = {v: False for v in g.vertex_set}

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

    for v in g.vertex_set:
        if has_cycle_util(g, v, visited, rec_stack):
            return True
    return False


g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(3, 1)  # has cycle
expected = True
actual = has_cycle(g)
print(expected == actual)
