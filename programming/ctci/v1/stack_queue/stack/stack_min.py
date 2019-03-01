import sys
import unittest


class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 1
        self.array = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize
        self.minvals = [sys.maxsize] * (stacksize * self.numstacks)

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def Min(self, stacknum):
        return self.minvals[self.IndexOfTop(stacknum)]

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        if self.IsEmpty(stacknum):
            self.minvals[self.IndexOfTop(stacknum)] = item
        else:
            self.minvals[self.IndexOfTop(stacknum)] = min(item, self.minvals[self.IndexOfTop(stacknum) - 1])
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value


class Test(unittest.TestCase):
    stack = MultiStack(10)
    stacknum = 0
    stack.Push(5, 0)
    stack.Push(6, 0)
    print("peek of stacknum {} : {}".format(stacknum, stack.Peek(stacknum)))
    print("min of stacknum {} : {}".format(stacknum, stack.Min(stacknum)))


if __name__ == "__main__":
    unittest.main()
