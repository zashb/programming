"""
prob: There are N children standing in a line. Each child is assigned a rating value. You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
Idea: 2 ptr
Comp: O(n)
"""


def get_min_candies(arr):
    n = len(arr)
    if n == 0:
        return 0
    candies = [1] * n
    # scan from left
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1
    # update result
    result = candies[n - 1]
    # scan from right
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
        # update result
        result += candies[i]
    return result


arr = [1, 0, 2]
expected = 5
actual = get_min_candies(arr)
print(expected == actual)

arr = [1, 2, 2]
expected = 4
actual = get_min_candies(arr)
print(expected == actual)
