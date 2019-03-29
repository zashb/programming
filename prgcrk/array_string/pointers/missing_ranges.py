"""
prob: given arr in inclusive range [lower, upper] find missing ranges
idea:
comp: O(n)
"""

import sys


def get_missing_ranges(arr, lower, upper):
    if not arr:
        return []
    res, n, start = [], len(arr), lower
    if lower == sys.maxsize:
        return res
    for i in range(n):
        # handling duplicates
        # the order is important tooR
        if i < n - 1 and arr[i] == arr[i + 1]:
            continue
        if arr[i] == start:
            start += 1
        else:
            res.append(format_range(start, arr[i] - 1))
            if arr[i] == sys.maxsize:
                return res
            start = arr[i] + 1
    if start <= upper:
        res.append(format_range(start, upper))
    return res


def format_range(lower, upper):
    if lower == upper:
        return str(lower)
    else:
        return str(lower) + "->" + str(upper)


arr = [0, 1, 3, 50, 75]
lower, upper = 0, 99
expected = ["2", "4->49", "51->74", "76->99"]
actual = get_missing_ranges(arr, lower, upper)
print(expected == actual)
