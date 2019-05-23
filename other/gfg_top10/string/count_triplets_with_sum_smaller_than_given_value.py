import unittest


def count_triplets_with_sum_smaller_than_given_value(nums, target):
    # sort
    nums.sort()
    result = 0
    # 3 ptr
    n = len(nums)
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] >= target:
                r -= 1
            else:
                result += r - l
                l += 1
    return result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = 4
        actual = count_triplets_with_sum_smaller_than_given_value([5, 1, 3, 4, 7], 12)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
