"""
prob: Given two strings s and t, write a function to determine if t is an anagram of s
idea: counter, pop
comp:
"""
from collections import Counter


def is_anagram(s, t):
    m, n = len(s), len(t)
    if m != n:
        return False
    if not s or not t:
        return False
    Map = Counter(s)
    # Map = dict()
    # for i in s:
    #     if i in Map:
    #         Map[i] += 1
    #     else:
    #         Map[i] = 1
    for i in range(m):
        if t[i] in Map:
            if Map[t[i]] == 1:
                # remember the pop step
                Map.pop(t[i])
            else:
                Map[t[i]] -= 1
        else:
            return False
    if len(Map) > 0:
        return False
    return True


expected = True
actual = is_anagram("hello", "lloeh")
print(expected == actual)

expected = False
actual = is_anagram("12121", "1234")
print(expected == actual)
