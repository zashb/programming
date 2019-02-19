import unittest

class MultiStack:
    def __init__(self, stacksize):
        self.numstacks = 3
        self.stacksize = stacksize
        self.array = [0] * (self.stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
    
    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def index_of_top(self, stacknum):
        # only logic to remember
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def push(self, item, stacknum):
        if self.is_full(stacknum):
            raise Exception("Stack {} is full".format(stacknum))
        self.sizes[stacknum] += 1
        self.array[self.index_of_top(stacknum)] = item

    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception("Stack {} is empty".format(stacknum))
        value = self.array[self.index_of_top(stacknum)]
        self.array[self.index_of_top(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value
    
    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception("Stack {} is empty".format(stacknum))
        return self.array[self.index_of_top(stacknum)]

class Test(unittest.TestCase):
    def test_multistack(self):
        stack = MultiStack(2)
        stacknum = 1
        print("is stacknum {} empty : {}".format(stacknum, stack.is_empty(stacknum)))
        stack.push(3, stacknum)
        print("is stacknum {} empty : {}".format(stacknum, stack.is_empty(stacknum)))
        print("peek of stacknum {} : {}".format(stacknum, stack.peek(stacknum)))
        stack.push(2, stacknum)
        print("peek of stacknum {} : {}".format(stacknum, stack.peek(stacknum)))
        stack.pop(stacknum)
        print("peek of stacknum {} after pop : {}".format(stacknum, stack.peek(stacknum)))

if __name__ == "__main__":
    unittest.main()
