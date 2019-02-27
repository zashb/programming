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


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string = "{()}[]"
        self.assertTrue(is_bal_paren(string))
        string = "{()}]"
        self.assertFalse(is_bal_paren(string))


if __name__ == '__main__':
    unittest.main()
