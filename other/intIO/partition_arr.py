"""
prob: partition array L into regions <k,=k,>k
idea:
comp:
"""


def partition_arr(arr, k):
    if not arr and not k:
        return -1
    if not arr or not k:
        return -1
    lp, rp, traverse = 0, len(arr) - 1, 0
    while traverse < rp:
        if arr[traverse] < k:
            arr[lp], arr[traverse] = arr[traverse], arr[lp]
            lp += 1
            traverse += 1
        elif arr[traverse] == k:
            traverse += 1
        else:
            rp -= 1
            arr[rp], arr[traverse] = arr[traverse], arr[rp]
    return arr


expected = [2, 1, 3, 4, 5]
actual = partition_arr([2, 4, 3, 1, 5], 3)
print(expected == actual)
