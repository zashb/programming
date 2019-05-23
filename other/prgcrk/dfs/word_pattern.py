"""
prob: Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str
Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
idea:
comp:
"""


def word_pattern(pattern, string):
    if not pattern or not string:
        return False
    arr = string.split(" ")
    if len(pattern) != len(arr):
        return False
    Map = dict()
    for i in range(len(pattern)):
        if pattern[i] in Map:
            if Map[pattern[i]] != arr[i]:
                return False
        elif arr[i] in Map.values():
            return False
        Map[pattern[i]] = arr[i]
    return True


actual = word_pattern("abba", "dog cat cat dog")
expected = True
print(expected == actual)
