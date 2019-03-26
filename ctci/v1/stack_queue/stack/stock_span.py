import unittest

from programming.ctci.v1.stack_queue.stack import StackList


def get_stock_span(price):
    # n = len(price)
    # stack = []
    # result = [0] * len(price)
    # for i in range(n):
    #     while len(stack) > 0 and price[stack[-1]] <= price[i]:
    #         stack.pop()
    #     result[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])
    #     stack.append(i)
    # return result

    """stack: push, pop, span computation"""
    n = len(price)
    stack = StackList()
    result = [0] * len(price)
    for i in range(n):
        while not stack.is_empty(stack.stack) and price[stack.stack[-1]] <= price[i]:
            stack.pop()
        if len(stack.stack) <= 0:
            result[i] = i + 1
        else:
            result[i] = i - stack.stack[-1]
        stack.push(i)
    return result


class Test(unittest.TestCase):
    def test_stock_span(self):
        price = [10, 4, 5, 90, 120, 80]
        actual = get_stock_span(price)
        print(actual)
