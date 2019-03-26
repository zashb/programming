class Solution:
    def maxProdSubArray(self,nums):
        # globalMax,localMax,localMin = float("-inf"), 1,1
        # for i in nums:
        #     if i > 0:
        #         localMax,localMin = localMax*i,localMin*i
        #     else:
        #         localMax,localMin=localMin*i,localMax*i
        #     globalMax = max(globalMax,localMax)
        # return globalMax
        if not nums:
            return 0
        currProd,maxProd = nums[0],float("-inf")
        for i in nums[1:]:
            currProd = max(i, currProd * i)
            maxProd = max(currProd, maxProd)

        return maxProd

if __name__ == "__main__":
    print(Solution().maxProdSubArray([2,3,-2,4]))
