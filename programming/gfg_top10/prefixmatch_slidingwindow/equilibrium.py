import unittest


def get_equilibrium_val(nums):
    total_sum = sum(nums)
    left_sum = 0
    # order of sub, checking, adding is imp
    for i in range(len(nums)):
        total_sum = total_sum - nums[i]
        if total_sum == left_sum:
            return i
        left_sum = left_sum + nums[i]
    return -1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [-7, 1, 5, 2, -4, 3, 0]
        expected = 3
        actual = get_equilibrium_val(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
