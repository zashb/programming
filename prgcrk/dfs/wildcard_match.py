"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

Const:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Idea:
1ptr each for s, p; ? is simple; * - starIdx, s_idx2
Ex:
s=aa, p=a, exp=False
s=adceb, p=a*c?b, exp=True
Comp: O(n)
"""


def is_matching(s, p):
    s_idx, p_idx, star_idx, s_idx2 = 0, 0, -1, -1
    while s_idx < len(s):
        if p_idx < len(p) and (p[p_idx] == "?" or p[p_idx] == s[s_idx]):
            s_idx += 1
            p_idx += 1
        elif p_idx < len(p) and p[p_idx] == "*":
            star_idx = p_idx
            s_idx2 = s_idx
            p_idx += 1
        elif star_idx != -1:
            p_idx = star_idx + 1
            s_idx = s_idx2 + 1
            s_idx2 += 1
        else:
            return False
    while p_idx < len(p) and p[p_idx] == "*":
        p_idx += 1
    return p_idx == len(p)


s, p, expected = "aa", "a", False
actual = is_matching(s, p)
print(expected == actual)
s, p, expected = "adceb", "a*c?b", True
actual = is_matching(s, p)
print(expected == actual)
