"""
prob: Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
idea: list of list intervals, update end of prev (hence lol instead of tuples), add to result in else
comp: O(n logn)
"""


def merge_intervals(intervals):
    # remeber to write base cases
    if intervals is None or len(intervals) == 1:
        return intervals
    intervals = sorted(intervals, key=lambda x: x[0])
    result, prev, n = [], 0, len(intervals)
    for i in range(n):
        if intervals[prev][1] > intervals[i][0]:
            # update end of prev
            intervals[prev][1] = max(intervals[prev][1], intervals[i][1])
        else:
            result.append(intervals[prev])
            prev = i
    result.append(intervals[prev])
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
expected = [[1, 6], [8, 10], [15, 18]]
actual = merge_intervals(intervals)
print(expected == actual)

intervals = [[1, 3], [2, 6], [8, 10], [15, 18], [4, 5]]
expected = [[1, 6], [8, 10], [15, 18]]
actual = merge_intervals(intervals)
print(expected == actual)
