# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space
import collections


class Solution:
    def majorityElem(self, nums):
        # ctr = collections.Counter()
        # for n in nums:
        #     ctr[n] += 1
        #     if len(ctr) == 3:
        #         a = collections.Counter(set(ctr))
        #         ctr -= a
        # return [n for n in ctr if nums.count(n) > len(nums) // 3]

        ctr = collections.Counter(nums)
        return [i for i in ctr if ctr[i] > len(nums) // 3]


if __name__ == "__main__":
    print(Solution().majorityElem([2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 7]))
