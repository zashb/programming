# #  find the length of the longest consecutive elements sequence
def longest_conseq_subarr(nums):
    s = set(nums)
    result = 0
    # check each possible sequence from the start then update optimal length
    for i in nums:
        # if current element is the starting element of a sequence
        if i - 1 not in s:
            # Then check for next elements in the sequence
            j = i
            while j in s:
                j = j + 1
            # update  optimal length if this length is more
            result = max(result, j - i)
    return result


nums = [1, 9, 3, 10, 4, 20, 2]
expected = 4
actual = longest_conseq_subarr(nums)
print(expected == actual)

#
# def lngstConsecSeq(n):
#     n_s = sorted(n)
#     res = []
#     for i, j in enumerate(n_s):
#         if j + 1 in n_s or j - 1 in res:
#             res.append(j)
#     return len(res)
#
#     # res, map = 0, {}
#     # for i in n:
#     #     if i not in map:
#     #         left = map[i - 1] if i - 1 in map else 0
#     #         right = map[i + 1] if i + 1 in map else 0
#     #         _sum = left + right + 1
#     #         map[i] = map[i - left] = map[i + right] = _sum
#     #         res = max(res, _sum)
#     #     else:
#     #         continue
#     # return res
#
#
# if __name__ == '__main__':
#     print(lngstConsecSeq([100, 4, 200, 1, 3, 2]))
#
# # algo
# # number_seqlen_map={},max_seqlen=0
# # if new elem: l=map[i-1],sly r, sum=l+r+1, map[i]=map[i-1]=map[i+1]=sum
# # else: continue
