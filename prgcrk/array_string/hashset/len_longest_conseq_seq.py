"""
prob: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive elements sequence should be [1, 2, 3, 4]. Its length is 4
idea:
comp:
"""


def len_longest_consec_seq(arr):
    n = len(arr)
    if not arr or n == 0:
        return arr
    Set, Max = set(), 1
    for i in arr:
        Set.add(i)
    for i in arr:
        l, r, count = i - 1, i + 1, 1
        while l in Set:
            count += 1
            Set.remove(l)
            l -= 1
        while r in Set:
            count += 1
            Set.remove(r)
            r += 1
        Max = max(Max, count)
    return Max


expected = 4
actual = len_longest_consec_seq([100, 4, 200, 1, 3, 2])
print(expected == actual)
