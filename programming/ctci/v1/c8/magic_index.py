import unittest


# distinct nums
def magic_index(nums):
    return searcher(nums, 0, len(nums) - 1)


def searcher(nums, s, e):
    if e < s:
        return -1
    mid = (s + e) // 2
    if nums[mid] == mid:
        return mid
    elif nums[mid] > mid:
        return searcher(nums, s, mid - 1)
    else:
        return searcher(nums, mid + 1, e)


# non-distinct nums
def magic_index2(nums):
    return searcher2(nums, 0, len(nums) - 1)


def searcher2(nums, s, e):
    if e < s:
        return -1
    mid = (s + e) // 2
    if nums[mid] == mid:
        return mid
    left = searcher2(nums, s, min(mid - 1, nums[mid]))
    if left >= 0:
        return left
    right = searcher2(nums, max(mid + 1, nums[mid]), e)
    return right


class Test(unittest.TestCase):
    def test_mi(self):
        nums = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
        actual = magic_index(nums)
        print(actual)

    def test_mi_2(self):
        nums = [-1, -1, 2, 2, 2, 4, 5, 7, 9, 12]
        # works for both distinct and non-distinct nums
        # nums = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
        actual = magic_index2(nums)
        print(actual)
