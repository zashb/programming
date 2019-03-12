"""
return max prod of 3 terms

Idea : prod of 3 max or 2 min and max
com : heapq.nlargest(n, iter), m=len(iter). O(log(n) * m)
"""

import heapq


def max_prod3(arr):
    l = heapq.nlargest(3, arr)
    s = heapq.nsmallest(2, arr)
    return max(l[0] * l[1] * l[2], s[0] * s[1] * l[0])


arr = [1, -2, 7, 3, 10, 1, 5]
expected = 350
actual = max_prod3(arr)
print(expected == actual)

arr = [-10, -20, 7, 3, 10, 1, 5]
expected = 2000
actual = max_prod3(arr)
print(expected == actual)
