# def subsets(nums):
#     res = [[]]
#     for i in nums:
#         res.extend([j + [i] for j in res])
#     return res
#
#
# print(subsets([1, 2, 3]))


# def subsets(nums):
#     res = []
#     backtrack(res, [], nums, 0)
#     return res
#
#
# def backtrack(res, temp, nums, start):
#     res.append(temp[:])
#     for i in range(start, len(nums)):
#         temp.append(nums[i])
#         backtrack(res, temp, nums, i + 1)
#         temp.pop()  # Backtrack
#
#
# print(subsets([1, 2, 3]))


# rem temp[:]

# def subWthDup(nums):
#     res = []
#     backtrack(res, [], nums, 0)
#     return res
#
#
# def backtrack(res, tmp, nums, start):
#     res.append(tmp[:])
#     for i in range(start, len(nums)):
#         if i > start and nums[i] == nums[i - 1]:
#             continue
#         tmp.append(nums[i])
#         backtrack(res, tmp, nums, i + 1)
#         tmp.pop()
#
#
# print(subWthDup([1, 1, 1, 2, 2, 3]))

# def perm(nums):
#     res = []
#     backtrack(res, [], nums)
#     return res
#
#
# def backtrack(res, tmp, nums):
#     if len(tmp) == len(nums):
#         res.append(tmp[:])
#     else:
#         for i in range(0, len(nums)):
#             if nums[i] in tmp:
#                 continue
#             tmp.append(nums[i])
#             backtrack(res, tmp, nums)
#             tmp.pop()
#
#
# print(perm([1, 2, 3]))

# def combSum(nums, target):
#     res = []
#     backtrack(res, [], nums, target, 0)
#     return res
#
#
# def backtrack(res, tmp, nums, remain, start):
#     if remain < 0:
#         return
#     elif remain == 0:
#         res.append(tmp[:])
#     else:
#         for i in range(start, len(nums)):
#             tmp.append(nums[i])
#             backtrack(res, tmp, nums, remain - nums[i], i)
#             tmp.pop()
#
# print(combSum([2,3,6,7],7))

# def palPart(s):
#     res = []
#     backtrack(res, [], s, 0)
#     return res
#
#
# def backtrack(res, tmp, s, start):
#     if start == len(s):
#         res.append(tmp[:])
#     else:
#         for i in range(start, len(s)):
#             if s[start:i+1] == s[start:i+1][::-1]:
#                 tmp.append(s[start:i+1])
#                 backtrack(res, tmp, s, i + 1)
#                 tmp.pop()
#
#
# print(palPart("aab"))
