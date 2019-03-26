class Solution:
    def trapRainWater(self, heights):
        # lp, rp, water, minHeight = 0, len(heights) - 1, 0, 0
        # while lp < rp:
        #     while lp < rp and minHeight >= heights[lp]:
        #         water += minHeight - heights[lp]
        #         lp += 1
        #     while lp < rp and minHeight >= heights[rp]:
        #         water += minHeight - heights[rp]
        #         rp -= 1
        #     minHeight = min(heights[lp], heights[rp])
        # return water

        n = len(heights)
        left, right, water = [0] * n, [0] * n, 0
        left[0] = heights[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], heights[i])
        # print(left)
        right[n - 1] = heights[n - 1]
        for i in range(n - 2, 0, -1):
            right[i] = max(right[i + 1], heights[i])
        # print(right)
        for i in range(n):
            water += min(left[i], right[i]) - heights[i]
        print(water)


if __name__ == "__main__":
    print(Solution().trapRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    # TTR:
    # init and outermost loop sim to cntnrWthMstWtr
    # minheight var, 2 ptrs at opp ends, 2 while loops one from each end and with each pointer
    # while lp<rp,wat=minheight-lp,lp+=1
    # while rp>lp,wat=minheight-rp,rp-=1
    # update minheight
