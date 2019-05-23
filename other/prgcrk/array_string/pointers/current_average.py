"""
prob : average from data stream
idea : math_prob
comp : O(n)
"""


def curr_avg(arr):
    res, n = 0, len(arr)
    for i in range(n):
        res = (res * i + arr[i]) / (i + 1)
        print(res)


arr = [10, 20, 30, 40, 50, 60]
curr_avg(arr)
