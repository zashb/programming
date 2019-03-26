import unittest


def get_min_platforms(a, d):
    """find minimum number of platforms required on a railway station"""
    a.sort()
    d.sort()
    ai, dj = 1, 0
    n = len(a)
    plat_needed, result = 1, 1
    while ai < n and dj < n:
        if a[ai] < d[dj]:
            plat_needed = plat_needed + 1
            ai += 1
            # result to store max plat_needed
            if plat_needed > result:
                result = plat_needed
        else:
            plat_needed = plat_needed - 1
            dj += 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [900, 940, 950, 1100, 1500, 1800]
        dep = [910, 1200, 1120, 1130, 1900, 2000]
        expected = 3
        actual = get_min_platforms(arr, dep)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
