from collections import Counter

"""
prob : wind in larger string that contains all char in smaller string
idea : slid wind
Time Complexity: O(|S| + |T|) where |S| and |T| represent the lengths of strings S and T. In the worst case we might end up visiting every element of string S twice, once by left pointer and once by right pointer. |T| represents the length of string T.

Space Complexity: O(|S| + |T|). ∣S∣ when the window size is equal to the entire string S. |T| when T has all unique characters
"""


def minWindow(s, t):
    if not t or not s:
        return ""
    # Dictionary which keeps a count of all the unique characters in t.
    dict_t = Counter(t)
    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)
    # left and right pointer
    l, r = 0, 0
    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    formed = 0
    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}
    # ans tuple of the form (window length, left, right)
    ans = (float("inf"), None, None)
    while r < len(s):
        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.setdefault(character, 0) + 1
        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]
            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            # Move the left pointer ahead, this would help to look for a new window.
            l += 1
            # Keep expanding the window once we are done contracting.
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


s, t = "ADOBECODEBANC", "ABC"
print(minWindow(s, t))

# import collections
#
#
# class Solution:
#     def minWindSubstr(self, s, t):
#         need, missing = collections.Counter(t), len(t)
#         i, I, J = 0, 0, 0
#         for idx, char in enumerate(s):
#             missing -= need[char] > 0
#             need[char] -= 1
#             if not missing:
#                 while i < idx and need[s[i]] < 0:
#                     need[s[i]] += 1
#                     i += 1
#                 if not J or idx - i <= J - I:
#                     I, J = i, idx
#         return s[I:J + 1]
#
#
# if __name__ == "__main__":
#     print(Solution().minWindSubstr("ADOBECODEBANC", "ABC"))
