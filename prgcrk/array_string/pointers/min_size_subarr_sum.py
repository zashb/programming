"""
prob: Given arr of +ve ints and a targetSum, find min length of subarray whose sum >= targetSum.
idea: 2ptr
Comp: O(n)
"""
import sys


def min_size_subarr_sum(arr, targetSum):
    left, right, Sum = 0, 0, 0
    min_len = sys.maxsize
    while right < len(arr):
        if Sum < targetSum:
            Sum += arr[right]
            right += 1
        else:
            min_len = min(min_len, right - left)
            if left == right - 1:
                return 1
            Sum -= arr[left]
            left += 1
    while Sum >= targetSum:
        min_len = min(min_len, right - left)
        Sum -= arr[left]
        left += 1
    return 0 if min_len == sys.maxsize else min_len


# def min_size_subarr_sum(arr, target):
#     left, right, Sum, n = 0, 0, 0, len(arr)
#     min_size = sys.maxsize
#     if target in arr:
#         return 1
#     while right < n:
#         Sum = Sum + arr[right]
#         while Sum >= target:
#             Sum = Sum - arr[left]
#             min_size = min(min_size, right - left + 1)
#             left = left + 1
#         right = right + 1
#     return min_size if min_size < sys.maxsize else -1


arr = [2, 3, 1, 2, 4, 3]
target = 7
expected = 2
actual = min_size_subarr_sum(arr, target)
print(expected == actual)
