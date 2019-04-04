"""
prob: Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
idea:
comp:
"""


def pal_pairs(words):
    # res = []
    # lp, rp = 0, 1
    # while lp < len(words):
    #     while rp < len(words):
    #         concWords = words[lp] + words[rp]
    #         if concWords == concWords[::-1] and lp != rp:
    #             res.append([lp, rp])
    #         rp += 1
    #     lp += 1
    #     rp = 0
    #
    # return res

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


expected = [[0, 1], [1, 0]]
actual = pal_pairs(["bat", "tab", "cat"])
print(expected == actual)

expected = [[0, 1], [1, 0], [3, 2], [2, 4]]
actual = pal_pairs(["abcd", "dcba", "lls", "s", "sssll"])
print(expected == actual)
