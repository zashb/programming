# O(n*k) solution for finding maximum sum of a subarray of size k
import sys
import unittest

INT_MIN = -sys.maxsize - 1


# Returns maximum sum in a subarray of size k.
def maxSum(arr, n, k):
    max_sum = INT_MIN
    # Consider all blocks starting with i.
    for i in range(n - k + 1):
        window = arr[i:i + k]
        current_sum = sum(window)
        # Update result if required. 
        max_sum = max(current_sum, max_sum)
    return max_sum


def max_sum_opt(nums, k):
    n = len(nums)
    if n < k:
        return -1
    # first window
    max_sum = sum(nums[:k])
    # Compute sums of remaining windows by removing first element of previous window and adding last element of current window.
    current_sum = max_sum
    for i in range(k, n):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum


class Test(unittest.TestCase):
    def test_maxSum(self):
        arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
        k = 4
        n = len(arr)
        expected = 24
        actual = maxSum(arr, n, k)
        print(expected == actual)
        actual = max_sum_opt(arr, k)
        print(expected == actual)
