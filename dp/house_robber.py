"""
prob: Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police. police will be alerted if two adjacent houses were broken into on the same night
idea:
comp:
"""


def house_robber(arr):
    if not arr or len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    dp = [float('-inf')] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
    return dp[len(arr) - 1]


# def house_robber(arr):
#     arr2 = arr.copy()
#     if not arr2:
#         return arr2
#     prev1, prev2 = 0, 0
#     for i in arr2:
#         prev1, prev2 = max(prev1, prev2 + i), prev1
#     return prev1


expected = 4
actual = house_robber([1, 2, 3, 1])
print(expected == actual)

expected = 12
actual = house_robber([2, 7, 9, 3, 1])
print(expected == actual)
