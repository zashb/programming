"""
prob: Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)
idea: map[Sum]:idx,
comp:
"""


def max_subarr_len(arr, target):
    n, Max, Sum, Map = len(arr), 0, 0, dict()
    if not arr or n == 1:
        return arr
    for i in range(n):
        Sum += arr[i]
        if Sum == target:
            Max = max(Max, i + 1)
        diff = Sum - target
        if diff in Map:
            Max = max(Max, i - Map[diff])
        if Sum not in Map:
            Map[Sum] = i
    return Max


expected = 4
actual = max_subarr_len([1, -1, 5, -2, 3], 3)
print(expected == actual)
