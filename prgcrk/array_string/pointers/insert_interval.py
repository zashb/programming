"""
prob: Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

idea: similar to merge_interval
comp: O(n logn)
"""


def insert_interval(intervals, interval):
    intervals.append(interval)
    intervals = sorted(intervals, key=lambda x: x[0])
    result, prev, n = [], 0, len(intervals)
    for i in range(n):
        if intervals[prev][1] > intervals[i][0]:
            intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
        else:
            result.append(intervals[prev])
            prev = i
    result.append(intervals[prev])
    return result


intervals = [[1, 3], [6, 9]]
interval = [2, 5]
expected = [[1, 5], [6, 9]]
actual = insert_interval(intervals, interval)
print(expected == actual)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
interval = [4, 9]
expected = [[1, 2], [3, 10], [12, 16]]
actual = insert_interval(intervals, interval)
print(expected == actual)
