import unittest


def get_nge(nums):
    n = len(nums)
    for i in range(n):
        nge = -1
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                nge = nums[j]
                break
        print("nge of {} is {}".format(nums[i], nge))


class Test(unittest.TestCase):
    def test_get_nge(self):
        nums = [11, 13, 21, 3]
        get_nge(nums)
