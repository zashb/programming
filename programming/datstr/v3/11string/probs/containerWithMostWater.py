# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of
# line i is at (i, ai) and (i, 0). Find two lines,
# which together with x-axis forms a container,
# such that the container contains the most water.
#
# Note: You may not slant the container.

class Solution:
    def maxArea(self, height):
        # lp, rp, max_area = 0, len(height) - 1, 0
        # while lp < rp:
        #     max_area = max(max_area, min(height[lp], height[rp]) * (rp - lp))
        #     if height[lp] < height[rp]:
        #         lp += 1
        #     else:
        #         rp -= 1
        # return max_area

        maxArea = 0
        for lp in range(len(height) - 1):
            for rp in range(lp + 1, len(height)):
                maxArea = max(maxArea, min(height[lp], height[rp]) * (rp - lp))
        print(maxArea)


if __name__ == "__main__":
    height = [1, 2, 3, 4, 3, 2, 1, 5]
    print(Solution().maxArea(height))

    # TTR:
    # lp=0,rp=len(height)-1
    # after computing max area, lp=lp+1 if height[lp]<height[rp] else rp=rp-1
