import itertools


def getMaxOfMins(nums):
    # consid all winds starting from size 1
    for windSize in range(1, len(nums) + 1):
        maxOfMinForCurrWindSize = nums[0]
        for windOfCurrWindSize in range(len(nums) - windSize + 1):
            minOfCurrWindSize = nums[windOfCurrWindSize]
            for j in range(1, windSize):
                if nums[windOfCurrWindSize + j] < minOfCurrWindSize:
                    minOfCurrWindSize = nums[windOfCurrWindSize + j]
            if minOfCurrWindSize > maxOfMinForCurrWindSize:
                maxOfMinForCurrWindSize = minOfCurrWindSize
        print(str(maxOfMinForCurrWindSize) + " ")


def getMAxOfMinOfAllCombs(nums):
    for i in range(1, len(nums)):
        combList = list(itertools.combinations(nums, i))
        print(combList)
        minOfEachComb = [min(i) for i in combList]
        print(minOfEachComb)
        maxOfMinOfEachComb = max(minOfEachComb)
        print(maxOfMinOfEachComb, "\n")


def getMaxOfMins_v2(nums):
    outerrp = 1
    while outerrp < len(nums) + 1:
        rp = outerrp
        lp = 0
        wind = []
        # select window
        while rp < len(nums) + 1:
            # nums[lp:rp] appends a slice of array not just the values
            wind.append(nums[lp:rp])
            # inc lp not just rp
            lp += 1
            rp += 1
        print(wind)
        minOfEachWind = [min(i) for i in wind]
        print(minOfEachWind)
        print(max(minOfEachWind))
        outerrp += 1


if __name__ == "__main__":
    # getMaxOfMins([10, 20, 30, 50, 10, 70, 30])
    # getMAxOfMinOfAllCombs([10, 20, 30, 50, 10, 70, 30])
    getMaxOfMins_v2([10, 20, 30, 50, 10, 70, 30])
