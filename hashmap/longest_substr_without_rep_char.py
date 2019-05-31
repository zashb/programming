"""
prob: Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
idea: hashmap
comp: O(n)
"""


def llswrc(string):
    if not string:
        return -1

    res, left = 0, 0
    Map = dict()
    for right in range(len(string)):
        if string[right] in Map:
            left = max(left, Map[string[right]])
        res = max(res, right - left + 1)
        Map[string[right]] = right + 1
    return res


actual = llswrc("abcabcbb")
expected = 3
print(actual == expected)

actual = llswrc("bbb")
expected = 1
print(actual == expected)

actual = llswrc("pwwkew")
expected = 3
print(actual == expected)
