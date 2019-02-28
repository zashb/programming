import unittest


def find_subarray_with_given_sum(nums, Sum):
    """Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number"""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if sum(nums[i:j + 1]) == Sum:
                # return "Sum found between indexes {} and {}".format(i, j)
                print("Sum found between indexes {} and {}".format(i, j))


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     nums = [15, 2, 4, 8, 9, 5, 10, 23]
    #     Sum = 23
    #     actual = find_subarray_with_given_sum(nums, Sum)
    #     expected = "Sum found between indexes 1 and 4"
    #     self.assertEqual(actual, expected)

    def test_something_2(self):
        nums = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
        Sum = 0
        find_subarray_with_given_sum(nums, Sum)


if __name__ == '__main__':
    unittest.main()
