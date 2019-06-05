"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
idea: DP
comp: O(n**3)
"""


def word_break(s, dic):
    if not dic:
        return -1
    dp = [""] * (len(s) + 1)
    initial = ""
    dp[0] = initial
    for i in range(1, len(s) + 1):
        List = list()
        for j in range(i):
            if len(dp[j]) > 0 and s[j:i] in dic:
                for k in dp[j]:
                    temp = '' if k == '' else ' '
                    List.append(k + temp + s[j:i])
        dp[i] = List
    return dp[len(s)]


actual = word_break("catsanddog", ["cat", "cats", "and", "sand", "dog"])
expected = ["cats and dog", "cat sand dog"]
print(expected == actual)
