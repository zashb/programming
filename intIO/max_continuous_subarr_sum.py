"""
return max sum of contin subarr
idea : cum sum, compare with max
compl : O(n)
"""


def max_contin_subarr_sum(arr):
    Sum, res = 0, 0
    for i in arr:
        Sum = max(i, Sum + i)
        res = max(res, Sum)
    return res


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
expected = 7
actual = max_contin_subarr_sum(arr)
print(expected == actual)
