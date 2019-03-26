"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length of 2 under the problem constraint.

idea : 2 ptr, move window by adding right elem and sub left elem
"""
import sys


def min_size_subarr_sum(arr, target):
    left, right, Sum, n = 0, 0, 0, len(arr)
    min_size = sys.maxsize
    if target in arr:
        return 1
    while right < n:
        Sum = Sum + arr[right]
        while Sum >= target:
            Sum = Sum - arr[left]
            min_size = min(min_size, right - left + 1)
            left = left + 1
        right = right + 1
    return min_size if min_size < sys.maxsize else -1


arr = [2, 3, 1, 2, 4, 3]
target = 7
expected = 2
actual = min_size_subarr_sum(arr, target)
print(expected == actual)
