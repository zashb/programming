"""
idea : sim to perm, except prefix=[]
"""


import unittest


def get_all_pal_part(s):
    res = []
    dfs([], s, res)
    return res


def dfs(prefix, remainder, res):
    if len(remainder) == 0:
        res.append(prefix)
    for i in range(1, len(remainder) + 1):
        before = remainder[:i]
        if isPal(before):
            after = remainder[i:]
            dfs(prefix + [before], after, res)


def isPal(s):
    return s == s[::-1]


class Test(unittest.TestCase):
    def test_get_all_pal_part(self):
        string = "nitin"
        expected = ""
        actual = get_all_pal_part(string)
        print(actual)
