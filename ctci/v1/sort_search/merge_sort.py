import unittest


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]
        merge_sort(L)
        merge_sort(R)
        li, ri, k = 0, 0, 0
        while li < len(L) and ri < len(R):
            if L[li] <= R[ri]:
                nums[k] = L[li]
                li += 1
            else:
                nums[k] = R[ri]
                ri += 1
            k += 1
        while li < len(L):
            nums[k] = L[li]
            li += 1
            k += 1
        while ri < len(R):
            nums[k] = R[ri]
            ri += 1
            k += 1
        return nums


class Test(unittest.TestCase):
    def test_merge_sort(self):
        nums = [12, 11, 13, 5, 6, 7]
        actual = merge_sort(nums)
        self.assertTrue(sorted(nums) == actual)
