import unittest

from programming.ctci.v1.c3.stack import StackList


def nge(nums):
    """if next > pop , print
        else, push"""
    stack = StackList()
    for i in nums:
        next = i
        if not stack.is_empty(stack.stack):
            element = stack.pop()
            while element < next:
                print(str(element) + " -- " + str(next))
                if stack.is_empty(stack.stack):
                    break
                element = stack.pop()
            if element > next:
                stack.push(element)
        stack.push(next)
    while not stack.is_empty(stack.stack):
        element = stack.pop()
        next = -1
        print(str(element) + " -- " + str(next))


class Test(unittest.TestCase):
    def test_nge(self):
        nums = [11, 13, 21, 3]
        nge(nums)
