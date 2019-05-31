"""
prob: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
idea: hashmap
comp: O(n)
"""


def get_2sum(arr, T):
    if not arr or not T:
        return -1
    Map = dict()
    for i in range(len(arr)):
        if (T - arr[i]) in Map:
            return [i, Map[T - arr[i]]]
        Map[arr[i]] = i
    return -1


expected = [1, 0]
actual = get_2sum([2, 7, 11, 15], 9)
print(expected == actual)
