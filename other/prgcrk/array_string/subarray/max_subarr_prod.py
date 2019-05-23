"""
prob: Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6
idea: This is similar to maximum subarray. Instead of sum, the sign of number affect the product value.
When iterating the array, each element has two possibilities: positive number or negative number. We need to track a minimum value, so that when a negative number is given, it can also find the maximum value. We define two local variables, one tracks the maximum and the other tracks the minimum
comp: O(n)
"""


def max_prod(arr):
    n = len(arr)
    if not arr or n == 1:
        return arr
    Max, Min = [float('-inf')] * n, [float('inf')] * n
    Max[0], Min[0], res = arr[0], arr[0], arr[0]
    for i in range(n):
        if arr[i] > 0:
            Max[i] = max(arr[i], Max[i - 1] * arr[i])
            Min[i] = min(arr[i], Min[i - 1] * arr[i])
        else:
            Max[i] = max(arr[i], Min[i - 1] * arr[i])
            Min[i] = min(arr[i], Max[i - 1] * arr[i])
        res = max(res, Max[i])
    return res


expected = 6
actual = max_prod([2, 3, -2, 4])
print(expected == actual)
