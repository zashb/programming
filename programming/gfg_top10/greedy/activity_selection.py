import unittest


def get_activities(s, f):
    """The following implementation assumes that the activities
    are already sorted according to their finish time. Prints a maximum set of activities that can be done by a
    single person, one at a time"""
    prev, n = 0, len(s)
    result = [prev]
    for i in range(n):
        if s[i] >= f[prev]:
            result.append(i)
            # current becomes prev
            prev = i
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = [1, 3, 0, 5, 8, 5]
        f = [2, 4, 6, 7, 9, 9]
        expected = [0, 1, 3, 4]
        actual = get_activities(s, f)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
