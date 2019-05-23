"""
prob: Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based

numbers={2, 7, 11, 15}, target=9
index1=0, index2=1
idea: map diff and elem to idx
comp:
"""


def two_sum(arr, target):
    n = len(arr)
    if not arr or n < 2:
        return [0, 0]
    Map = dict()
    for i in range(n):
        if arr[i] in Map:
            return [Map[arr[i]], i]
        else:
            Map[target - arr[i]] = i
    return [0, 0]


expected = [0, 1]
actual = two_sum([2, 7, 11, 15], 9)
print(expected == actual)
