import bisect
import unittest


def binary_search(nums, key):
    nums.sort()
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if key == nums[mid]:
            return mid
        if key < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def bs_2(nums, key):
    nums.sort()
    # bisect_left returns idx of first occurence if elem exists else returns idx of rightmost elem < elem
    idx = bisect.bisect_left(nums, key)
    if nums[idx] == key:
        return "First occurence of {} found at index {}".format(key, idx)
    return "{} is not found in the list, it can be inserted at index {}".format(key, idx)


# adding bisect_right just for sake of completeness. ignore this
def bs_3(nums, key):
    nums.sort()
    # bisect_left returns idx of first occurence if elem exists else returns idx of rightmost elem < elem
    idx = bisect.bisect_right(nums, key)
    if nums[idx - 1] == key:
        return "{} found at index {}".format(key, idx - 1)
    return "{} can be inserted at index {}".format(key, idx)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [2, 3, 4, 10, 40]
        key = 10
        expected = 3
        actual = binary_search(nums, key)
        self.assertEqual(expected, actual)

    def test_something2(self):
        nums = [2, 3, 4, 10, 10, 40]
        key = 10
        actual = bs_2(nums, key)
        print(actual)
        key = 11
        actual = bs_2(nums, key)
        print(actual)

    # adding bisect_right just for sake of completeness. ignore this
    def test_something3(self):
        nums = [2, 3, 4, 10, 10, 40]
        key = 10
        actual = bs_3(nums, key)
        print(actual)
        key = 11
        actual = bs_3(nums, key)
        print(actual)


if __name__ == '__main__':
    unittest.main()
