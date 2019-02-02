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


def generate_parenthesis(n):
    """Intuition:
    To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.
    Consider the closure number of a valid parentheses sequence S: the least index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. Clearly, every parentheses sequence has a unique closure number. We can try to enumerate them individually.

    Algorithm:
    For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1. Then, the 2*c elements between must be a valid sequence, plus the rest of the elements must be a valid sequence."""
    if n == 0:
        return ['']
    ans = []
    for c in range(n):
        for left in generate_parenthesis(c):
            for right in generate_parenthesis(n - 1 - c):
                ans.append('({}){}'.format(left, right))
    return ans


def generate_parenthesis2(n):
    res = []
    generater(res, 2 * n, "", n, n)
    return res


def generater(res, n, tmp, left_rem, right_rem):
    if left_rem < 0 or left_rem > right_rem:
        return
    if left_rem == 0 and right_rem == 0:
        res.append(tmp)
        return
    generater(res, n - 1, tmp + "(", left_rem - 1, right_rem)
    generater(res, n - 1, tmp + ")", left_rem, right_rem - 1)


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

    def test_all_parens(self):
        n = 3
        actual = generate_parenthesis(n)
        print("generated parenthesis for n={} are : {}".format(n, actual))
        actual = generate_parenthesis2(n)
        print("generated parenthesis for n={} are : {}".format(n, actual))
