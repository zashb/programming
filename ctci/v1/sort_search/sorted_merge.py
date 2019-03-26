import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        NA = -1
        a = [10, 12, 13, 14, 18, NA, NA, NA, NA, NA]
        n = 5
        b = [16, 17, 19, 20, 22]
        m = 5
        actual = sorted_merge(a, b, n, m)
        print("\nsorted : {}".format(actual))


def sorted_merge(a, b, n, m):
    i, j = n - 1, m - 1
    last_idx = n + m - 1
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[last_idx] = a[i]
            i -= 1
        else:
            a[last_idx] = b[j]
            j -= 1
        last_idx -= 1
    return a


if __name__ == '__main__':
    unittest.main()
