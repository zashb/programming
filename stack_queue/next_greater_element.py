def get_nge(nums):
    n = len(nums)
    for i in range(n):
        nge = -1
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                nge = nums[j]
                break
        print("nge of {} is {}".format(nums[i], nge))


nums = [11, 13, 21, 3]
actual = get_nge(nums)
expected = """nge of 11 is 13
nge of 13 is 21
nge of 21 is -1
nge of 3 is -1"""
