class Solution:
    def countOfGreaterThanNums(self, nums):
        # lp, rp = 0, 1
        # res = []
        # while lp < len(nums):
        #     count = 0
        #     while rp < len(nums):
        #         if nums[rp] > nums[lp]:
        #             count += 1
        #         rp += 1
        #     res.append(count)
        #     lp += 1
        #     rp = lp + 1
        # return res

        # v2 using for loop
        res = []
        for lp in range(len(nums)):
            cnt = 0
            for rp in range(lp + 1, len(nums)):
                if nums[rp] > nums[lp]:
                    cnt += 1
            res.append(cnt)
        return res


if __name__ == "__main__":
    print(Solution().countOfGreaterThanNums([5, 3, 9, 8, 2, 6]))
