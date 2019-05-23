# def srchInsPos(n, t):
#     n_s = sorted(n)
#     if t < n_s[0]:
#         # n_s = [t] + n_s
#         return 0
#     if t > n_s[-1]:
#         # n_s += [t]
#         return len(n_s)
#     i, j = 0, len(n)
#     while i < j:
#         mid = (i + j) // 2
#         if t > n[mid]:
#             i = mid + 1
#         else:
#             j = mid
#     return i  # can return i or j


# # cool and beauty
# def srchInsPos(n, t):
#     return len([i for i in n if i < t])

import bisect


def srchInsPos(nums, key):
    nums.sort()
    # bisect_left returns idx of first occurence if elem exists else returns idx of rightmost elem < elem
    idx = bisect.bisect_left(nums, key)
    if idx < len(nums) and nums[idx] == key:
        return "First occurence of {} found at index {}".format(key, idx)
    return "{} is not found in the list, it can be inserted at index {}".format(key, idx)


if __name__ == '__main__':
    print(srchInsPos([1, 3, 5, 6], 0))
    print(srchInsPos([1, 3, 5, 6], 7))
    print(srchInsPos([1, 3, 5, 6], 5))
    print(srchInsPos([1, 3, 5, 6], 2))

# algo
# i,j=0,len
# while i<j: m=(i+j)//2, compare with t and inc/dec i/j 
# return j
