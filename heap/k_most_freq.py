"""
prob:
idea: counter O(n), heapify O(n logn), n largest combines heapify and kth largest O(n logn)
comp:
"""
import heapq
from collections import Counter


def k_most_freq(arr, k):
    count = Counter(arr)
    res = heapq.nlargest(k, count.keys(), key=count.get)
    return res


expected = [1, 2]
actual = k_most_freq([1, 1, 1, 2, 2, 3], 2)
print(expected == actual)
