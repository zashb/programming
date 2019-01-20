class Solution:
    def countGreaterVals(self, nums):
        lp, rp = 0, 1
        res = []
        while lp < len(nums):
            count = 0
            while rp < len(nums):
                if nums[rp] > nums[lp]:
                    count += 1
                rp += 1
            res.append(count)
            lp += 1
            rp = lp + 1
        return res


if __name__ == "__main__":
    print(Solution().countGreaterVals([5, 3, 9, 8, 2, 6]))
