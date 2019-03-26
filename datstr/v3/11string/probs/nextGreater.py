def getNextGreater(nums):
    # for i in range(len(nums)):
    #     nextGreaterVal = -1
    #     for j in range(i + 1, len(nums)):
    #         if nums[j] > nums[i]:
    #             nextGreaterVal = nums[j]
    #             break
    #     print(str(nums[i]) + " -- " + str(nextGreaterVal))

    # v2
    for lp in range(len(nums)):
        if lp == len(nums) - 1:
            print(str(nums[lp]) + "-- -1")
        else:
            for rp in range(lp + 1, len(nums)):
                # next greatest
                if nums[rp] > nums[lp]:
                    print(str(nums[lp]) + "--" + str(nums[rp]))
                    break
                else:
                    # continue and it reached EOL, then -- -1
                    if rp == len(nums) - 1:
                        print(str(nums[lp]) + "-- -1")


if __name__ == "__main__":
    getNextGreater([11, 13, 21, 3])

    # TTR:
    # rem the idea of initializing nextGreaterVal
