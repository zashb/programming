import unittest


class MyTestCase(unittest.TestCase):
    """
    Python program to find n-th stair using step size 1 or 2 or 3.
    Returns count of ways to reach n-th  stair using 1 or 2 or 3 steps"""

    def test_something(self):
        n = 4
        actual = find_step(n)
        print("count of ways to reach n = {} step is : {}".format(n, actual))

    def test_dp(self):
        n = 4
        actual = find_step_dp(n)
        print("count of ways to reach n = {} step is : {}".format(n, actual))


def find_step_dp(n):
    result = [0] * (n + 1)
    result[0], result[1], result[2] = 1, 1, 2
    for i in range(3, n + 1):
        result[i] = result[i - 1] + result[i - 2] + result[i - 3]
    return result[n]


def find_step(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return find_step(n - 1) + find_step(n - 2) + find_step(n - 3)


if __name__ == '__main__':
    unittest.main()
