"""
prob: Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not)
idea: iterate and check each char
comp: O(n)
"""


def is_subsequence(s, t):
    if not s and not t:
        return False
    if not t and s:
        return True
    if not s and t:
        return False
    si, ti = 0, 0
    while si < len(s) and ti < len(t):
        if s[si] == t[ti]:
            si += 1
        ti += 1
        if si == len(s):
            return True
    return False


expected = True
actual = is_subsequence("ace", "abcde")
print(expected == actual)

expected = False
actual = is_subsequence("aec", "abcde")
print(expected == actual)

expected = True
actual = is_subsequence("abc", "abcde")
print(expected == actual)
