import numpy as np


class Solution:
    def maxSlidingWind(self, nums, k):
        # lp = 0
        # rp = lp + k
        # maxWind = []
        # while rp < len(nums) + 1:
        #     maxWind.append(max(nums[lp:rp]))
        #     lp += 1
        #     rp = lp + k
        # return maxWind

        # v2 using for loop
        lp = 0
        res = []
        for rp in range(lp + k, len(nums) + 1):
            res.append(max(nums[lp:rp]))
            lp += 1
        return res

    def medianSlidingWind(self, nums, k):
        # lp = 0
        # rp = lp + k
        # medWind = []
        # while rp < len(nums) + 1:
        #     wind = sorted(nums[lp:rp])
        #     windLen = len(wind)
        #     # if windLen % 2 != 0:
        #     #     medWind.append(wind[(windLen + 1) // 2 - 1])
        #     medWind.append(wind[(windLen + 1) // 2 - 1])
        #     lp += 1
        #     rp = lp + k
        # return medWind

        # v2 using for loop
        lp = 0
        res = []
        for rp in range(lp + k, len(nums) + 1):
            wind = sorted(nums[lp:rp])
            windlen = len(wind)
            if windlen % 2 != 0:
                res.append(wind[(windlen + 1) // 2 - 1])
            else:
                res.append(np.mean(wind[windlen // 2 - 1], wind[windlen // 2 + 1]))
            lp += 1
        return res


if __name__ == "__main__":
    print(Solution().maxSlidingWind([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(Solution().medianSlidingWind([1, 3, -1, -3, 5, 3, 6, 7], 3))

    # TTR:
    # sorted(wind)
    # median = window[len +1 //2-1]
