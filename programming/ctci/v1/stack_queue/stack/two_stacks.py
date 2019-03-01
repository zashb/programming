import unittest


class TwoStacks:
    """
    stack1 : [0]=-1, push=increment, pop=decrement
    stack2 : [0]=size, push=decrement, pop=increment
    """

    def __init__(self, n):
        self.size = n
        self.list = [None] * self.size
        self.top1 = -1
        self.top2 = self.size

    def push1(self, item):
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.list[self.top1] = item
        else:
            return "stack overflow"

    def push2(self, item):
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.list[self.top2] = item
        else:
            return "stack overflow"

    def pop1(self):
        if self.top1 >= 0:
            item = self.list[self.top1]
            self.top1 -= 1
            return item

    def pop2(self):
        if self.top2 <= self.size:
            item = self.list[self.top2]
            self.top2 += 1
            return item


class Test(unittest.TestCase):
    def test_twostacks(self):
        ts = TwoStacks(5)
        print(ts.top1, ts.top2)
        ts.push1(5)
        ts.push2(10)
        ts.push2(15)
        ts.push1(11)
        ts.push2(7)
        print(ts.top1, ts.top2)
        print("Popped element from stack1 is " + str(ts.pop1()))
        print(ts.top1, ts.top2)
        ts.push2(40)
        print(ts.top1, ts.top2)
        print("Popped element from stack2 is " + str(ts.pop2()))
        print(ts.top1, ts.top2)
