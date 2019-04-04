"""
prob: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4], the contiguous subarray [4,−1,2,1] has the largest sum = 6.
idea: DP
Let f(n) be the maximum subarray for an array with n elements.
f(n) = { f(n-1)>0 ? f(n-1) : 0 } + nums[n-1]
f(0) = 0
f(1) = nums[0]

comp: O(n)
"""


def max_subarr_sum(arr):
    if not arr or len(arr) == 1:
        return arr
    res, Sum = arr[0], arr[0]
    for i in arr:
        if Sum <= 0:
            Sum = i
        else:
            Sum += i
        res = max(res, Sum)
    return res


expected = 6
actual = max_subarr_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(expected == actual)
