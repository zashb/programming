import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [10, 90, 49, 2, 1, 5, 23]
        actual = get_peaks_valleys(nums)
        print(actual)
        actual = get_peaks_valleys2(nums)
        print(actual)


def get_peaks_valleys(nums):
    sorted_nums = sorted(nums)
    for i in range(1, len(nums), 2):
        sorted_nums[i - 1], sorted_nums[i] = sorted_nums[i], sorted_nums[i - 1]
    return sorted_nums


def get_peaks_valleys2(nums):
    n = len(nums)
    for i in range(0, n, 2):
        # If current even element is smaller than previous 
        if i > 0 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

        # If current even element is smaller than next
        if i < n - 1 and nums[i] < nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


if __name__ == '__main__':
    unittest.main()
