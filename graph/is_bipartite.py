"""
prob: Given an undirected graph, return true if and only if it is bipartite.
Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
idea: BFS
comp: O(V+E)
"""

# from graph.graph_class import Graph
from graph_class import Graph
from collections import deque

class Solution(object):
    def is_bipartite(self, graph):
        colored = dict()
        for i in range(len(graph)):
            if i not in colored and graph[i]:
                colored[i] = 1
                q = deque([i])
                while q:
                    cur = q.popleft()
                    for nb in graph[cur]:
                        if nb not in colored:
                            colored[nb] = -colored[cur]
                            q.append(nb)
                        elif colored[nb] == colored[cur]:
                            return False
        return True

actual = Solution().is_bipartite([[1,3], [0,2], [1,3], [0,2]])
expected = True
print(actual == expected)
actual = Solution().is_bipartite([[1,2,3], [0,2], [0,1,3], [0,2]])
expected = False
print(actual == expected)
