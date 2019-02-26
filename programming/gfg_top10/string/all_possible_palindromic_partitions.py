import unittest


def get_all_pal_part(s):
    res = []
    dfs(s, [], res)
    return res


def dfs(s, path, res):
    if not s:
        res.append(path)
    for i in range(1, len(s) + 1):
        if isPal(s[:i]):
            dfs(s[i:], path + [s[:i]], res)


def isPal(s):
    return s == s[::-1]


class Test(unittest.TestCase):
    def test_get_all_pal_part(self):
        string = "nitin"
        expected = ""
        actual = get_all_pal_part(string)
        print(actual)
