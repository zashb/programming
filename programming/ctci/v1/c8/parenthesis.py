import unittest


def valid_parenthesis(string):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for i in string:
        if i in mapping:
            top = stack.pop() if stack else "#"
            if mapping[i] != top:
                return False
        else:
            stack.append(i)
    return not stack


def check_valid_parenthesis_with_wildchar(string):
    lo = hi = 0
    for c in string:
        lo += 1 if c == '(' else -1
        hi += 1 if c != ')' else -1
        if hi < 0: break
        lo = max(lo, 0)
    return lo == 0


def remove_invalid_par(string):
    level = {string}
    while True:
        is_v = list(filter(is_valid, level))
        if is_v:
            return is_v
        for string in level:
            for i in range(len(string)):
                level.add(string[:i] + string[i + 1:])


def is_valid(string):
    ctr = 0
    for c in string:
        if c == '(':
            ctr += 1
        elif c == ')':
            ctr -= 1
            if ctr < 0:
                return False
    return ctr == 0


class Test(unittest.TestCase):
    def test_vp(self):
        cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
        for case in cases:
            actual = valid_parenthesis(case)
            print("is {} valid : {}".format(case, actual))

    def test_cvs(self):
        cases = ["()", "(*)", "(*))"]
        for case in cases:
            actual = check_valid_parenthesis_with_wildchar(case)
            print("is {} valid : {}".format(case, actual))

    def test_rip(self):
        cases = ["()())()", "(a)())()", ")("]
        for case in cases:
            actual = remove_invalid_par(case)
            print("removing invalid parenthesis for {} gives : {}".format(case, actual))
