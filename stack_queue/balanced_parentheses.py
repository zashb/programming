import unittest


def is_bal_paren(string):
    stack = []
    mapping = {"}": "{", "]": "[", ")": "("}
    for i in string:
        if i in mapping:
            if not stack:
                return False
            elif stack.pop() != mapping[i]:
                return False
        else:
            stack.append(i)
    return not stack


expected = True
actual = is_bal_paren("{()}[]")
print(expected == actual)

expected = False
actual = is_bal_paren("{()}]")
print(expected == actual)
