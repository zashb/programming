"""
prob: Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] find the minimum number of conference rooms required.
idea: The basic idea of the solution is that we sequentially assign meeting to a room. We use a min heap to track the earliest ending meeting. Whenever an old meeting ends before a new meeting starts, we remove the old meeting. Otherwise, we need an extra room
prob:
"""
import heapq


def meeting_rooms(arr):
    n = len(arr)
    if not arr or n == 1:
        return arr
    arr.sort(key=lambda x: x[0])
    pq = []
    for i in arr:
        # if the new meeting happens after the earliest meeting ends, replace the earliest ending meeting with the new meeting
        if pq and i[0] >= pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, i[1])
        else:
            heapq.heappush(pq, i[1])
    return len(pq)


expected = 2.
actual = meeting_rooms([[0, 30], [5, 10], [15, 20]])
print(expected == actual)
