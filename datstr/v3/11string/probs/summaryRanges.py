class Solution:
    def summaryRanges(self, nums):
        nums = sorted(nums)
        # lp, rp = 0, 1
        # res = []
        # while rp < len(nums):
        #     if nums[lp:rp + 1] == list(range(nums[lp], nums[rp] + 1)):
        #         rp += 1
        #     else:
        #         res.append(str(nums[lp]) + "->" + str(nums[rp - 1]))
        #         lp = rp
        #         rp += 1
        # if str(nums[-1]) not in res:
        #     res += str(nums[-1])
        # return res

        # v2 using for
        lp = 0
        res = []
        for rp in range(lp + 1, len(nums)):
            if nums[lp:rp + 1] == list(range(nums[lp], nums[rp] + 1)):
                continue
            res.append(str(nums[lp]) + "->" + str(nums[rp - 1]))
            lp = rp
        if str(nums[-1]) not in res:
            res += str(nums[-1])
        return res

        # improved v2
        # def summRange(self, nums):
        #     lp, stEndIdxDict = 0, {}
        #     for rp in range(lp + 1, len(nums)):
        #         if nums[lp:rp + 1] == list(range(nums[lp], nums[rp] + 1)):
        #             stEndIdxDict[lp] = rp
        #         else:
        #             lp = rp
        #     res = []
        #     for k, v in stEndIdxDict.items():
        #         res.append(str(nums[k]) + " - " + str(nums[v]))
        #     res.append(str(nums[-1]))
        #     return(res)


if __name__ == "__main__":
    print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
    print(Solution().summaryRanges([0,2,3,4,6,8,9]))
