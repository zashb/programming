from collections import deque


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# BFS approach
class Solution:
    def cloneGraph(self, node):
        if not node:
            return
        # copy node label
        nodeCopy = UndirectedGraphNode(node.label)
        # map node in orig:clone
        visitedDic = {node: nodeCopy}
        # enqueue node
        queue = deque([node])
        while queue:
            # dequeue first node
            node = queue.popleft()
            # for each neighbor the popped node
            for neighbor in node.neighbors:
                # if the neighbor is not already visited,
                if neighbor not in visitedDic:
                    # copy the label
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    # create a mapping in visitedDic
                    visitedDic[neighbor] = neighborCopy
                    # make neighborCopy as neighbors of node in clone
                    visitedDic[node].neighbors.append(neighborCopy)
                    # append the current neighbor to queue
                    queue.append(neighbor)
                else:
                    visitedDic[node].neighbors.append(visitedDic[neighbor])
        return nodeCopy
