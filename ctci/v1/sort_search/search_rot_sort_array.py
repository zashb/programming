import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        nums = [4, 5, 6, 7, 8, 9, 1, 2, 3]
        key = 6
        low, high = 0, len(nums) - 1
        actual = search(nums, low, high, key)
        print("index : {}".format(actual))
        nums = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
        key = 5
        low, high = 0, len(nums) - 1
        actual = search(nums, low, high, key)
        print("index : {}".format(actual))


def search(nums, low, high, key):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == key:
        return mid
    # If nums[low...mid] is sorted
    if nums[low] <= nums[mid]:
        # As this subarray is sorted, we can quickly check if key lies in half or other half
        if nums[low] <= key <= nums[mid]:
            return search(nums, low, mid - 1, key)
        return search(nums, mid + 1, high, key)
    # If nums[low..mid] is not sorted, then nums[mid... r] must be sorted
    if nums[mid] <= key <= nums[high]:
        return search(nums, mid + 1, high, key)
    return search(nums, low, mid - 1, key)


if __name__ == '__main__':
    unittest.main()
