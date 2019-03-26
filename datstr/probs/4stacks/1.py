class Stack:
    # commented - handle overflow
    def __init__(self,limit = 10):
        self.stk = []
        # self.stk = [None] * limit
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) == 0

    def push(self,item):
        if len(self.stk) >= self.limit:
            print("stack overflow")
            # self.resize()
            # self.stk.append(item)
        else:
            self.stk.append(item)

    def pop(self):
        if len(self.stk) == 0:
            print("stack underflow")
        else:
            return self.stk.pop()

    def peek(self):
        if len(self.stk) == 0:
            print("stack underflow")
        else:
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def resize(self):
        newStk = list(self.stk)
        self.limit = 2 * self.limit
        self.stk = newStk


class Solution:
    def checkParenMatch(self,inp):
        matches = {")":"(","}":"{","]":"["}
        s = Stack()
        for i in inp:
            if i in matches.values():
                s.push(i)
            else:
                if s.isEmpty():
                    return False
                else:
                    a = s.pop()
                if a != matches[i]:
                    return False
        return True

class SmartStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def stack_push(self,item):
        self.stack.append(item)
        # if min[] is empty or item < min[-1]
        if item <= self.stack_min() or not self.min:
            self.min.append(item)
        else:
            self.min.append(self.min[-1])

    def stack_pop(self):
        a = self.stack.pop()
        self.min.pop()
        return a

    def stack_min(self):
        return self.min[-1]

class RemoveAdjDup:
    def remAdjDup(self,str):
        stkptr = -1
        size = len(str)
        i=0
        while i < size:
            # if element on stack != current elem, add to stack
            if stkptr == -1 or str[stkptr] != str[i]:
                stkptr += 1
                str[stkptr] = str[i]
                i += 1
            else:
                # if ==, skip elements
                while i < size and str[stkptr] == str[i]:
                    i += 1
                stkptr -= 1
        stkptr += 1
        str = str[0:stkptr]
        return str


if __name__ == "__main__":
    # s = Stack()
    # print(s.isEmpty())
    # for i in range(11,16):
    #     s.push(i)
    # print(s.stk)
    # print(s.pop())
    # print(s.peek())

    # print(Solution().checkParenMatch("({[})"))

    # s = SmartStack()
    # for i in [11,12,3,3,3,3333,0]:
    #     s.stack_push(i)
    # print(s.stack_min())

    print(RemoveAdjDup().remAdjDup(list("careermonk")))
