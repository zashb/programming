"""
prob: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array
Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
idea: bin search, sorted arr
comp: O(logn)
"""


def search_insert(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    if target > arr[n - 1]:
        return n
    while l < r:
        mid = (l + r) // 2
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid
    return l


arr, target, expected = [1, 3, 5, 6], 5, 2
actual = search_insert(arr, target)
print(expected == actual)
arr, target, expected = [1, 3, 5, 6], 2, 1
actual = search_insert(arr, target)
print(expected == actual)
arr, target, expected = [1, 3, 5, 6], 7, 4
actual = search_insert(arr, target)
print(expected == actual)
arr, target, expected = [1, 3, 5, 6], 0, 0
actual = search_insert(arr, target)
print(expected == actual)
