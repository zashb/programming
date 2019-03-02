import unittest

from programming.ctci.v1.stack_queue.stack.stack import StackList


def balanced(exp):
    stack = StackList()
    matching = {"}": "{", ")": "(", "]": "["}
    for i in exp:
        if i not in matching:
            stack.push(i)
        else:
            if not stack.is_empty(stack.stack):
                return stack.pop() == matching[i]


class Test(unittest.TestCase):
    def test_bal_par(self):
        exp = '{()}[]'
        self.assertTrue(balanced(exp))
        exp = "[()]{}{[()()]()}"
        self.assertTrue(balanced(exp))
        exp = "[(])"
        self.assertFalse(balanced(exp))
        exp = ")"
        self.assertFalse(balanced(exp))
