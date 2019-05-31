"""
prob: Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

idea: hashmap
comp: O(n)
"""
from collections import Counter


def first_uniq_char(string):
    if not string:
        return -1
    c = Counter(string)
    for i in range(len(string)):
        if c[string[i]] == 1:
            return i
    return -1


actual = first_uniq_char("leetcode")
expected = 0
print(expected == actual)

actual = first_uniq_char("loveleetcode")
expected = 2
print(expected == actual)
