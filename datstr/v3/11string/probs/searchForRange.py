class Solution:
    def searchRange(self, nums, target):
        # lp, rp = 0, 0
        # while rp < len(nums):
        #     if nums[lp] != target:
        #         lp += 1
        #     else:
        #         if rp < lp:
        #             rp = lp
        #         if nums[rp] == target:
        #             rp += 1
        #         else:
        #             return [lp, rp - 1]

        # v2 for loop
        res = []
        for lp in range(len(nums)):
            if nums[lp] == target:
                for rp in range(lp + 1, len(nums)):
                    if nums[rp] == target:
                        continue
                    else:
                        res.append([lp, rp - 1])
                    break
        return res


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 7, 8, 10], 7))
