import unittest


def get_max(nums, k):
    """Given an array of integers and a number k, find maximum sum of a subarray of size k."""
    n = len(nums)
    all_subarray_sum = []
    for i in range(n):
        subarray = nums[i:i + k]
        subarray_sum = sum(subarray)
        all_subarray_sum.append(subarray_sum)
    return max(all_subarray_sum)


def get_max_optim(nums, k):
    n = len(nums)
    if n < k:
        return "invalid"
    res = 0
    # sum of 1st window
    for i in range(k):
        res = res + nums[i]
    # Compute sums of remaining windows by removing first element of previous window and adding last element of current window
    curr_sum = res
    for i in range(k, n):
        curr_sum = curr_sum + nums[i] - nums[i - k]
        res = max(res, curr_sum)
    return res


def get_sum(arr):
    """
    Given an array of n numbers, our task is to calculate the maximum subarray sum, i.e., the largest possible sum of a sequence of consecutive values in the
array
    """
    best, Sum, n = 0, 0, len(arr)
    for i in range(n):
        Sum = max(arr[i], Sum + arr[i])
        best = max(best, Sum)
    return best


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [1, 4, 2, 10, 2, 3, 1, 0, 20]
        k = 4
        expected = 24
        actual = get_max(nums, k)
        self.assertEqual(actual, expected)
        actual = get_max_optim(nums, k)
        self.assertEqual(actual, expected)

    def test(self):
        arr = [-2, -3, 4, -1, -2, 1, 5, -3]
        expected = 7
        actual = get_sum(arr)
        print(expected == actual)


if __name__ == '__main__':
    unittest.main()
