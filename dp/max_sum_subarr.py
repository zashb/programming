def maxSubArray(nums):
    if not nums:
        return 0
    currSum = maxSum = nums[0]
    for i in nums[1:]:
        currSum = max(i, currSum + i)
        maxSum = max(currSum, maxSum)

    return maxSum


expected = 6
actual = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(expected == actual)
