import unittest


class MyTestCase(unittest.TestCase):
    """
    Python program to find n-th stair using step size 1 or 2 or 3.
    Returns count of ways to reach n-th  stair using 1 or 2 or 3 steps"""

    def test_something(self):
        n = 3
        actual = find_step(n)
        print("count of ways to reach n = {} step is : {}".format(n, actual))

    def test_dp(self):
        n = 3
        actual = find_step_dp(n)
        print("count of ways to reach n = {} step is : {}".format(n, actual))

    def test_get_first_n_fib(self):
        n = 10
        actual = get_first_n_fib(n)
        print("first {} fib num : {}".format(n, actual))


def get_first_n_fib(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


def find_step_dp(n):
    result = [0] * (n + 1)
    result[0], result[1], result[2] = 1, 1, 2
    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[n]


def find_step(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return find_step(n - 1) + find_step(n - 2)


if __name__ == '__main__':
    unittest.main()
