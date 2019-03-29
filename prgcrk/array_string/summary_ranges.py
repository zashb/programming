"""
Given a sorted integer array without duplicates, return the summary of its ranges.
idea: 2 ptr, print_range
comp: O(n)
"""


def summary_ranges(arr):
    if not arr:
        return []
    res, left, right = [], 0, 0
    while right < len(arr) - 1:
        if arr[right] + 1 != arr[right + 1]:
            res.append(format_range(arr[left], arr[right]))
            left = right + 1
        right += 1
    res.append(format_range(arr[left], arr[right]))
    return res


def format_range(l, r):
    if l == r:
        return str(l)
    else:
        return str(l) + "->" + str(r)


arr = [0, 1, 2, 4, 5, 7]
expected = ["0->2", "4->5", "7"]
actual = summary_ranges(arr)
print(expected == actual)

arr = [0, 2, 3, 4, 6, 8, 9]
expected = ["0", "2->4", "6", "8->9"]
actual = summary_ranges(arr)
print(expected == actual)
