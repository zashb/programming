import collections


class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * len(self.graph)
        queue = collections.deque()
        # key repetitive steps enqueue the node and mark it as visited
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.popleft()
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.bfs(2)
