# # return minimum size of subarray that can produce the given sum
#
# def minSizSubarrSum(nums, target):
#     if not nums or len(nums)==0:  return 0
#     i,j,_sum,_min=0,0,0,99999
#     while j<len(nums):
#         _sum+=nums[j]
#         j+=1
#         while _sum>=target:
#             _min=min(_min,j-i)
#             _sum-=nums[i]
#             i+=1
#     return 0 if _min==99999 else _min
#
# if __name__ == '__main__':
#     print(minSizSubarrSum([2, 3, 1, 2, 4, 3], 7))

import sys


def min_size_subarray_sum(nums, target):
    left, Sum = 0, 0
    result = sys.maxsize
    for right in range(len(nums)):
        Sum = Sum + nums[right]
        while Sum >= target:
            result = min(result, right - left + 1)
            Sum = Sum - nums[left]
            left = left + 1
    return result if result < sys.maxsize else -1


nums = [2, 3, 1, 2, 4, 3]
Sum = 7
expected = 2
actual = min_size_subarray_sum(nums, Sum)
print(expected == actual)
