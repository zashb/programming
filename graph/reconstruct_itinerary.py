"""
prob: Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK
Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].But it is larger in lexical order.
idea: dfs, stack of airports
comp: O(V+E)
"""

from graph.graph_class import Graph


def find_itinerary(tickets):
    if not tickets:
        return -1

    graph = Graph()
    res = []

    for ticket in tickets:
        graph.add_edge(ticket[0], ticket[1])

    def dfs(v):
        while graph.graph[v]:
            destination = graph.graph[v].pop()
            dfs(destination)
        res.append(v)

    dfs('JFK')
    return res[::-1]


expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
actual = find_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print(expected == actual)
