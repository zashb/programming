import unittest


def get_len_lcs(x, y):
    m, n = len(x), len(y)
    if m == 0 or n == 0:
        return 0
    elif x[m - 1] == y[n - 1]:
        return 1 + get_len_lcs(x[: len(x) - 1], y[: len(y) - 1])
    else:
        return max(get_len_lcs(x, y[: len(y) - 1]), get_len_lcs(x[: len(x) - 1], y))


def get_len_lcs_tab(x, y):
    # goes in reverse
    m, n = len(x), len(y)
    dp = [[None for j in range(n + 1)] for i in range(m + 1)]
    # L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[m][n]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = "AGGTAB"
        y = "GXTXAYB"
        expected = 4
        actual = get_len_lcs(x, y)
        self.assertEqual(expected, actual)
        actual = get_len_lcs_tab(x, y)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
