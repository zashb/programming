"""
find max len of cont subarr with equal num of 0 and 1

Idea : get all subarr and count 0 and 1
comp : O(n^2)
Ex :
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""


def max_len_cont_subarr(arr):
    res, n = 0, len(arr)
    for lp in range(n):
        zeros, ones = 0, 0
        # for each continuous subarr
        for rp in range(lp, n):
            if arr[rp] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                res = max(res, rp - lp + 1)
    return res


arr = [0, 1]
expected = 2
actual = max_len_cont_subarr(arr)
print(expected == actual)

arr = [0, 1, 0]
expected = 2
actual = max_len_cont_subarr(arr)
print(expected == actual)
