import unittest


def get_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    # Create a table to store results of subproblems
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):
            # If first array_string is empty, only option is to insert all characters of second array_string
            if i == 0:
                dp[i][j] = j  # Min. operations = j
            # If second array_string is empty, only option is to remove all characters of second array_string
            elif j == 0:
                dp[i][j] = i  # Min. operations = i
            # If last characters are same, ignore last char and recur for remaining array_string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # If last character are different, consider all possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # Insert
                                   dp[i - 1][j],  # Remove
                                   dp[i - 1][j - 1])  # Replace
    return dp[m][n]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s1 = "sunday"
        s2 = "saturday"
        expected = 3
        actual = get_edit_distance(s1, s2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
