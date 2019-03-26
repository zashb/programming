import collections


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        visited = [False] * len(self.graph)

        def _dfsUtil(s, visited):
            visited[s] = True
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    _dfsUtil(i, visited)

        _dfsUtil(s, visited)


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.dfs(2)
