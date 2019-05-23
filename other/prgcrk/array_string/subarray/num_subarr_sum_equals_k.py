"""
prob: Given an array of integers and an integer k, find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
idea: map Sum:count
comp:
"""


def num_subarr_eq_k(arr, target):
    if not arr or len(arr) == 1:
        return arr
    Map, count, Sum = {0: 1}, 0, 0
    for i in arr:
        Sum += i
        count += Map.setdefault(Sum - target, 0)
        Map[Sum] = Map.setdefault(Sum, 0) + 1
    return count


expected = 2
actual = num_subarr_eq_k([1, 1, 1], 2)
print(expected == actual)
