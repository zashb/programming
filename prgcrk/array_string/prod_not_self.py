"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]
For example, given [1,2,3,4], return [24,12,8,6].

Idea: overall prod divided by each number

"""


def prod_not_self(arr):
    prod, res, n = 1, [], len(arr)
    for i in range(n):
        res.append(prod)
        prod *= arr[i]
    prod = 1
    for i in range(n - 1, -1, -1):
        res[i] = res[i] * prod
        prod *= arr[i]
    return res


arr = [1, 2, 3, 4]
expected = [24, 12, 8, 6]
actual = prod_not_self(arr)
print(expected == actual)
