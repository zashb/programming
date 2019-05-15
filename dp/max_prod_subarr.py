def max_prod_subarr(nums):
    if not nums:
        return 0
    currProd, maxProd = nums[0], float("-inf")
    for i in nums[1:]:
        currProd = max(i, currProd * i)
        maxProd = max(currProd, maxProd)

    return maxProd


expected = 6
actual = max_prod_subarr([2, 3, -2, 4])
print(expected == actual)
