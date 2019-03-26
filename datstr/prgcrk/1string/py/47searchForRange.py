import bisect

def main(nums,target):
    # def search(n):
    #     lo, hi = 0, len(nums)
    #     while lo < hi:
    #         mid = (lo + hi) // 2
    #         if nums[mid] >= n:
    #             hi = mid
    #         else:
    #             lo = mid + 1
    #     return lo
    # lo = search(target)
    # return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]

    lo,hi=bisect.bisect_left(nums, target),bisect.bisect_right(nums, target)-1
    return [lo,hi] if target in nums[lo:lo+1] else [-1, -1]

if __name__ == '__main__':
    nums=[5, 7, 7, 8, 8, 10]
    print(main(nums,8))