"""
prob:
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
idea:
if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
comp: O(V+E)
"""
from gfg_top10.graph.Graph import Graph


def can_finish(num_courses, prereq):
    visited = {v: 0 for v in range(num_courses)}
    graph = Graph()
    for i, j in prereq:
        graph.add_edge(i, j)

    def dfs(v):
        if visited[v] == -1:
            return False
        if visited[v] == 1:
            return True
        visited[v] = -1
        for adj_v in graph.graph[v]:
            if not dfs(adj_v):
                return False
        visited[v] = 1
        return True

    for i in range(num_courses):
        if not dfs(i):
            return False
    return True


expected = True
actual = can_finish(2, [[1, 0]])
print(expected == actual)

expected = False
actual = can_finish(2, [[1, 0], [0, 1]])
print(expected == actual)
