"""
prob: Given two arrays, write a function to compute their intersection.
Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
idea: counters intersection, ord_flag
comp: O(n)
"""

from collections import Counter


def m1(arr1, arr2):
    return list((Counter(arr1) & Counter(arr2)).elements())


expected = [2, 2]
actual = m1([1, 2, 2, 1], [2, 2])
print(expected == actual)


def m2(arr1, arr2):
    ord_flag, res = [0] * 128, []
    for i in arr1:
        ord_flag[ord(str(i))] += 1
    for i in arr2:
        if ord_flag[ord(str(i))] != 1:
            res.append(i)
    return res


expected = [2, 2]
actual = m2([1, 2, 2, 1], [2, 2])
print(expected == actual)
