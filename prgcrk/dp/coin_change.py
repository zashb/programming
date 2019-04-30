"""
prob: given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1
idea: dp
comp: O(S*n). On each step the algorithm finds the next F(i)F(i) in nn iterations, where 1\leq i \leq S1≤i≤S. Therefore in total the iterations are S*nS∗n.
"""


def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i], dp[i - j] + 1)
    return -1 if dp[amount] > amount else dp[amount]


expected = 3
actual = coin_change([1, 2, 5], 11)
print(expected == actual)
