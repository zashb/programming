import unittest


def count_dist(nums, k):
    """Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k"""
    n = len(nums)
    for i in range(n + 1 - k):
        win = nums[i: i + k]
        print(len(set(win)))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [1, 2, 1, 3, 4, 2, 3]
        k = 4
        count_dist(nums, k)


if __name__ == '__main__':
    unittest.main()
