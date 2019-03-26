def threeSum(nums):
    # c = itertools.combinations(nums,3)
    # s = {tuple(sorted(i)):i for i in c if sum(i)==0}
    # return list(s.keys())

    res = []
    nums = sorted(nums)
    for i in range(len(nums)):
        f, b, t = i + 1, len(nums) - 1, -nums[i]
        while f < b:
            sum = nums[f] + nums[b]
            if sum < t:
                f += 1
            elif sum > t:
                b -= 1
            else:
                triplet = [""] * 3
                triplet[0], triplet[1], triplet[2] = nums[i], nums[f], nums[b]
                res.append(triplet)
                while f < b and nums[f] == triplet[1]:
                    f += 1
                while f < b and nums[b] == triplet[2]:
                    b -= 1
        while i + 1 < len(nums) and nums[i + 1] == nums[i]:
            i += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, 4]))
