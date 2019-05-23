"""
prob: Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
idea:
comp:
"""


# def pal_pairs(words):
#     res = []
#     lp, rp = 0, 1
#     while lp < len(words):
#         while rp < len(words):
#             concWords = words[lp] + words[rp]
#             if concWords == concWords[::-1] and lp != rp:
#                 res.append([lp, rp])
#             rp += 1
#         lp += 1
#         rp = 0
#
#     return res


def pal_pairs(words):
    res = []
    for lp in range(len(words)):
        for rp in range(lp + 1, len(words)):
            concWord = words[lp] + words[rp]
            concWord2 = words[rp] + words[lp]
            if concWord == concWord[::-1] and lp != rp:
                res.append([lp, rp])
            if concWord2 == concWord2[::-1] and lp != rp:
                res.append([rp, lp])
    return res


# # optimization with lookup
# def pal_pairs(words):
#     if not words or len(words) == 1:
#         return words
#     Map = {words[i]: i for i in range(len(words))}
#     res = []
#     for i in range(len(words)):
#         for j in range(len(words[i])):
#             left, right = words[i][:j], words[i][j:]
#             if left == left[::-1]:
#                 rev_right = right[::-1]
#                 if rev_right in Map and Map[rev_right] != i:
#                     res.append([Map[rev_right], i])
#             if right == right[::-1]:
#                 rev_left = left[::-1]
#                 if rev_left in Map and Map[rev_left] != i and len(right) != 0:
#                     res.append([Map[rev_left], i])
#     return res


expected = [[0, 1], [1, 0]]
actual = pal_pairs(["bat", "tab", "cat"])
print(expected == actual)

expected = [[0, 1], [1, 0], [3, 2], [2, 4]]
actual = pal_pairs(["abcd", "dcba", "lls", "s", "sssll"])
print(expected == actual)
