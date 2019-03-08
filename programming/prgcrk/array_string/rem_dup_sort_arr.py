"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length. Do not allocate extra space for another array, you must do this in place with constant memory.
For example, given input array A = [1,1,2], your function should return length = 2, and A is now [1,2].

Constraints: len > 2
Ideas: set
Complexity: O(n)
"""


def rem_dup(arr):
    if len(arr) < 2:
        return len(arr)
    return len(set(arr))


# algo to rem dup without set
def rem_dup2(arr):
    if len(arr) < 2:
        return len(arr)
    left, right = 0, 1
    while right < len(arr):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]
        right += 1
    return left + 1


arr = [1, 1, 2]
expected = 2
actual = rem_dup(arr)
print(expected == actual)
actual = rem_dup2(arr)
print(expected == actual)
