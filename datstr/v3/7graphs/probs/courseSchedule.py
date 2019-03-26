from collections import deque


# BFS from front to end
class Solution:
    # def canFinish(self, numOfCourses, prereqs):
    #     # create a fwd map for numOfCourses
    #     forward = {i: set() for i in range(numOfCourses)}
    #     # see note for usages
    #     backward = defaultdict(set)
    #     # for each course and its prereq
    #     for i, j in prereqs:
    #         # make this struc - {1:{2}} - numofcourses:prereqs
    #         forward[i].add(j)
    #         # prereq:numofcourses
    #         backward[j].add(i)
    #     queue = deque([i for i in range(numOfCourses) if not backward[i]])
    #     count = 0
    #     while queue:
    #         node = queue.popleft()
    #         count += 1
    #         for neighbor in forward[node]:
    #             backward[neighbor].remove(node)
    #             if not backward[neighbor]:
    #                 queue.append(neighbor)
    #     return count == numOfCourses

    def canFinish(self, n, prereq):
        ind = [[] for _ in range(n)]  # indegree
        oud = [0] * n  # outdegree
        for p in prereq:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = deque()
        for i in range(n):
            if oud[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            x = dq.popleft()
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        return k == n

print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(2, [[1,0],[0,1]]))

# note
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('red', 1)]
# d = defaultdict(set)
# for k, v in s:
#     d[k].add(v)
# d
# Out[16]:
# defaultdict(set, {'blue': {2, 4}, 'red': {1}, 'yellow': {1, 3}})

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
# d
# Out[18]:
# defaultdict(list, {'blue': [2, 4], 'red': [1, 1], 'yellow': [1, 3]})
