"""
prob: Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.You may assume no duplicate exists in the array.
idea: If we pick the middle element, we can compare the middle element with the leftmost (or rightmost) element. If the middle element is less than leftmost, the left half should be selected; if the middle element is greater than the leftmost (or rightmost), the right half should be selected. Using recursion or iteration, this problem can be solved in time log(n).
In addition, in any rotated sorted array, the rightmost element should be less than the left-most element, otherwise, the sorted array is not rotated and we can simply pick the leftmost element as the minimum
comp: O(logn)
"""


def min_rot_sort_arr(arr):
    n = len(arr)
    if not arr or n == 0:
        return -1
    l, r = 0, n - 1
    while l <= r:
        # handling duplicates
        while arr[l] == arr[r] and l != r:
            l += 1
        if arr[l] <= arr[r]:
            return arr[l]
        mid = (l + r) // 2
        if arr[mid] >= arr[l]:
            l = mid + 1
        else:
            r = mid
    return -1


expected = 1
actual = min_rot_sort_arr([2, 1])
print(expected == actual)

expected = 1
actual = min_rot_sort_arr([2, 3, 1])
print(expected == actual)

expected = 1
actual = min_rot_sort_arr([2, 3, 3, 1])
print(expected == actual)
