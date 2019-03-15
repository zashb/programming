"""
prob : longest substr without rep char
idea : https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
com : O(n + d) where n is length of the input string and d is number of characters in input string alphabet. For example, if string consists of lowercase English characters then value of d is 26
"""


def lswrc(string):
    n, max_len, curr_len, prev_idx, i = len(string), 1, 1, 0, 0
    visited = [-1] * 128
    visited[ord(string[0])] = 0
    for i in range(1, n):
        prev_idx = visited[ord(string[i])]
        if i - prev_idx > curr_len:
            curr_len += 1
        else:
            if curr_len > max_len:
                max_len = curr_len
            curr_len = i - prev_idx
        visited[ord(string[i])] = i
    if curr_len > max_len:
        max_len = curr_len
    return max_len

# from timeit import default_timer as timer
#
#
# class Solution:
#     def longstSubstrWthtRepChar(self, s):
#         # lp, lens = 0, []
#         # for rp in range(lp + 1, len(s)):
#         #     if s[rp] not in s[lp:rp]:
#         #         continue
#         #     else:
#         #         lens.append(len(s[lp:rp]))
#         #         lp = rp
#         # return max(lens)
#
#         if len(s) == 0:
#             return 0
#         d, m, j = {}, 0, 0
#         for i in range(len(s)):
#             print(i)
#             if s[i] in d:
#                 j = max(j, d[s[i]] + 1)
#             d[s[i]] = i
#             m = max(m, i - j + 1)
#             print(d,"\t",m,"\t",j)
#         return m
#
#
# if __name__ == "__main__":
#     s = Solution()
#     # a = timer()
#     # print(s.longstSubstrWthtRepChar("abcabcbb"))
#     # b = timer()
#     # print(round(b-a,ndigits=4))
#     print(s.longstSubstrWthtRepChar("abcabcbb"))
