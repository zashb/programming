"""
prob: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Idea:
d is an array that contains booleans
d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.
Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
comp: O(n^2)
"""


# def check_word_split(string, dic):
#     n = len(string)
#     word_check = [False] * n
#     for i in range(n):
#         for w in dic:
#             nw = len(w)
#             if w == string[i - nw + 1:i + 1] and (word_check[i - nw] == True or i - nw == -1):
#                 word_check[i] = True
#     return word_check[-1]

# def check_word_split(string, dic):
#     n = len(string)
#     word_check = [False] * (n + 1)
#     word_check[0] = True
#     for fp in range(1, n + 1):
#         for bp in range(fp - 1, -1, -1):
#             if word_check[fp]:
#                 break
#             if word_check[bp]:
#                 if string[bp:fp] in dic:
#                     word_check[fp] = True
#     return word_check[-1]


# string = "applepenapple"
# dic = {"apple", "pen"}
# expected = True
# actual = check_word_split(string, dic)
# print(expected == actual)
#
# string = "apple"
# dic = {"appl", "aaple", "e"}
# expected = True
# actual = check_word_split(string, dic)
# print(expected == actual)

# class Solution:
#     def wordBreak(self,s,words):
#         d = [False]*len(s)
#         for i in range(len(s)):
#             for j in words:
#                 if j ==s[i-len(j)+1:i+1] and (d[i-len(j)] or i-len(j)==-1):
#                     d[i]=True
#
#         return d[-1]
#
#
# if __name__=="__main__":
#     print(Solution().wordBreak("leetcode",["leet","code"]))
#     print(Solution().wordBreak("leetcode",["le","etcode"]))
#     print(Solution().wordBreak("leetcode",["le","tcode"]))


def word_break(string, dic):
    if not string or not dic:
        return -1
    dp = [-1] * (len(string) + 1)
    dp[0] = 0
    for i in range(len(string)):
        if dp[i] != -1:
            for j in range(i + 1, len(string) + 1):
                if string[i:j] in dic:
                    dp[j] = i
    return dp[len(string)] != -1


actual = word_break("leetcode", ["leet", "code"])
expected = True
print(expected == actual)

actual = word_break("applepenapple", ["apple", "pen"])
expected = True
print(expected == actual)

actual = word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
expected = False
print(expected == actual)
