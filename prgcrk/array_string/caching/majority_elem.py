"""
prob: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. (assume that the array is non-empty and the majority element always exist in the array.)
idea: Assuming the majority exists and since the majority always takes more than half of space, the middle element is guaranteed to be the majority. Sorting array takes O(nlog(n)). So the time complexity of this solution is nlog(n).
idea: This problem can be solved in time of O(n) with constant space complexity. The basic idea is that the majority element can negate all other element's count.
comp:
"""


def majority_elem(arr):
    n = len(arr)
    if not arr or n == 0:
        return arr
    if n == 1:
        return arr[0]
    arr.sort()
    return arr[n // 2]


expected = 2
actual = majority_elem([1, 2, 3, 2, 2])
print(expected == actual)


def majority_elem2(arr):
    n = len(arr)
    if not arr or n == 0:
        return arr
    if n == 1:
        return arr[0]
    res, count = 0, 0
    for i in arr:
        if count == 0:
            res = i
            count = 1
        elif res == i:
            count += 1
        else:
            count -= 1
    return res


expected = 2
actual = majority_elem2([1, 2, 3, 2, 2])
print(expected == actual)
