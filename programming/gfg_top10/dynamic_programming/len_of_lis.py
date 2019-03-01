import unittest


def get_len_of_lis(nums):
    n = len(nums)
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    return max(lis)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [10, 22, 9, 33, 21, 50, 41, 60]
        expected = 5
        actual = get_len_of_lis(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
