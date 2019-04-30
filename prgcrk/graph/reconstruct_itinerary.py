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
comp:
"""
from collections import defaultdict


def findItinerary(tickets):
    # targets = defaultdict(list)
    # sorted_tickets = sorted(tickets, key=lambda x: x[0])
    # for a, b in sorted_tickets:
    #     targets[a].append(b)
    # route = []
    #
    # def visit(airport):
    #     while targets[airport]:
    #         destination = targets[airport].pop()
    #         visit(destination)
    #     route.append(airport)
    #
    # visit('JFK')
    # return route[::-1]

    if not tickets:
        return -1
    sd_dic, res = defaultdict(list), []
    for s, d in tickets:
        sd_dic[s].append(d)

    def dfs(s):
        while sd_dic[s]:
            d = sd_dic[s].pop()
            dfs(d)
        res.append(s)

    dfs('JFK')
    return res[::-1]


expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
actual = findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print(expected == actual)
