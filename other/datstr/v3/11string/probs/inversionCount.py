def getInversionCount(nums):
    n = len(nums)
    invCount = 0
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                invCount += 1
    return invCount

    # lp = 0
    # rp = lp + 1
    # while lp < n:
    #     while rp < n:
    #         if nums[lp] > nums[rp]:
    #             invCount += 1
    #         rp += 1
    #     lp += 1
    #     rp = lp + 1
    # return invCount


if __name__ == "__main__":
    print(getInversionCount([1, 20, 6, 4, 5]))
