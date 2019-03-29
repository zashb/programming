"""
Given an array and a value, remove all instances of that value in place and return the new length

Idea - for loop, 2ptr
"""


def rem_all_occu(arr, item):
    # # for loop
    # return len([elem for elem in arr if elem != item])
    # 2ptr
    left, right = 0, 0
    while right < len(arr):
        if arr[right] != item:
            arr[left] = arr[right]
            left += 1
        right += 1
    return left


arr = [1, 2, 3, 4, 2, 2, 3]
item = 2
expected = 4
actual = rem_all_occu(arr, item)
print(expected == actual)
