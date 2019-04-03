"""
prob: bin search imp
comp: O(logn)
"""


def bin_search(arr, target):
    n = len(arr)
    l, r = 0, n - 1
    while l < r:
        mid = (l + r) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1


expected = 2
actual = bin_search([1, 2, 3, 4, 5], 3)
print(expected == actual)
