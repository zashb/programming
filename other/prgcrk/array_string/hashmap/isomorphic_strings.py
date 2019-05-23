"""
prob: Given two strings s and t, determine if they are isomorphic. Two strings are isomorphic if the characters in s can be replaced to get t.

For example,"egg" and "add" are isomorphic, "foo" and "bar" are not
idea: We can define a map which tracks the char-char mappings. If a value is already mapped, it can not be mapped again.
comp: O(n)?
"""


# def are_isomorphic(s, t):
#     if not s or not t:
#         return False
#     if len(s) != len(t):
#         return False
#     d1, d2 = {}, {}
#     for i in range(len(s)):
#         d1[s[i]] = d1.get(s[i], []) + [i]
#         d2[t[i]] = d2.get(t[i], []) + [i]
#     return sorted(d1.values()) == sorted(d2.values())

def are_isomorphic(s1, s2):
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    d1, d2 = dict(), dict()
    for i in range(len(s1)):
        if s1[i] in d1:
            if d1[s1[i]] != s2[i]:
                return False
        else:
            if s2[i] in d2:
                return False
            d1[s1[i]] = s2[i]
            d2[s2[i]] = s1[i]
    return True


expected = True
actual = are_isomorphic("egg", "add")
print(expected == actual)

expected = False
actual = are_isomorphic("foo", "bar")
print(expected == actual)

expected = False
actual = are_isomorphic("bar", "foo")
print(expected == actual)
