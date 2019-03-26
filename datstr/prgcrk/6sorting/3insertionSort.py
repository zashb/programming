def insertionSort(nums):
    for i in range(1, len(nums)):
        currVal = nums[i]
        while i > 0 and nums[i - 1] > currVal:
            nums[i] = nums[i - 1]
            i -= 1
        nums[i] = currVal
    return nums

if __name__=="__main__":
    print(insertionSort([54,26,93,17,77,31,44,55,20]))