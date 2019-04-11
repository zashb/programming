"""
prob: minimum spanning tree
idea: prim
comp: O(V^2)
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for c in range(self.V)] for r in range(self.V)]


def print_mst(parent):
    print("Edge \tWeight")
    for i in range(1, g.V):
        print(parent[i], "-", i, "\t", g.graph[i][parent[i]])


# A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
def minKey(key, mstSet):
    min = float('inf')
    for v in range(g.V):
        if key[v] < min and not mstSet[v]:
            min = key[v]
            min_index = v
    return min_index


# Function to construct and print MST for a graph represented using adjacency matrix representation
def primMST(g):
    # Key values used to pick minimum weight edge in cut
    key = [float('inf')] * g.V
    parent = [None] * g.V  # Array to store constructed MST
    # Make key 0 so that this vertex is picked as first vertex
    key[0] = 0
    mstSet = [False] * g.V
    parent[0] = -1  # First node is always the root of
    for cout in range(g.V):
        # Pick the minimum distance vertex from the set of vertices not yet processed. u is always equal to src in first iteration
        u = minKey(key, mstSet)
        # Put the minimum distance vertex in the shortest path tree
        mstSet[u] = True
        # Update dist value of the adjacent vertices of the picked vertex only if the current distance is greater than new distance and the vertex in not in the shotest path tree
        for v in range(g.V):
            # graph[u][v] is non zero only for adjacent vertices of m mstSet[v] is false for vertices not yet included in MST Update the key only if graph[u][v] is smaller than key[v]
            if 0 < g.graph[u][v] < key[v] and not mstSet[v]:
                key[v] = g.graph[u][v]
                parent[v] = u

    print_mst(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]

primMST(g)
# expected =
# Edge 	Weight
# 0 - 1 	 2
# 1 - 2 	 3
# 0 - 3 	 6
# 1 - 4 	 5
