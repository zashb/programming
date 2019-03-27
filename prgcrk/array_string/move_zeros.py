"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
"""


def move_zeros_2(arr):
    left, right = 0, 0
    while right < len(arr):
        if arr[right] == 0:
            right += 1
        else:
            arr[left] = arr[right]
            left += 1
            right += 1
    while left < len(arr):
        arr[left] = 0
        left += 1
    return arr


arr = [0, 1, 0, 3, 12]
expected = [1, 3, 12, 0, 0]
actual = move_zeros_2(arr)
print(expected == actual)

# def move_zeros(arr):
#     zero_idx = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             # to ensure we are not swapping when all num are non-zero
#             if arr[zero_idx] != 0:
#                 arr[i], arr[zero_idx] = arr[zero_idx], arr[i]
#             zero_idx += 1
#     return arr
#
#
# arr = [0, 1, 0, 3, 12]
# expected = [1, 3, 12, 0, 0]
# actual = move_zeros(arr)
# print(expected == actual)
