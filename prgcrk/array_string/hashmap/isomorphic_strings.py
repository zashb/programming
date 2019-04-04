"""
prob: Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not
idea: We can define a map which tracks the char-char mappings. If a value is already mapped, it can not be mapped again.
comp: O(n)?
"""


def are_isomorphic(s, t):
    m, n = len(s), len(t)
    if m != n:
        return False
    if not m or not n:
        return False
    map_s, map_t = dict(), dict()
    for i in range(m):
        if s[i] in map_s:
            if t[i] != map_s[s[i]]:
                return False
        else:
            if t[i] in map_t:
                return False
            map_s[s[i]] = t[i]
            map_t[t[i]] = s[i]
    return True


expected = True
actual = are_isomorphic("egg", "add")
print(expected == actual)

expected = False
actual = are_isomorphic("foo", "bar")
print(expected == actual)
