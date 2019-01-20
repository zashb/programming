# ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
# ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
import operator
import collections


class Solution:
    def fun(self, s):
        # oprDict = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.floordiv}
        # deq = collections.deque()
        # for i in s:
        #     if i not in oprDict:
        #         i = int(i)
        #         deq.append(i)
        #     else:
        #         b = deq.pop()
        #         a = deq.pop()
        #         deq.append(oprDict[i](a,b))
        # return list(deq)
        stack = []
        for i in s:
            if i in "+-*/":
                b, a = stack.pop(), stack.pop()
                # eval takes str as inp and ret calc, repr is req for eval
                i = repr(int(eval(a + i + b)))
            # without the comma, its an extend; hence when "13" it appends as "1","3"; , basically says to append instead of extend
            # stack.append(i)
            stack += i,
        return int(stack[0])


if __name__ == "__main__":
    print(Solution().fun(["2", "1", "+", "3", "*"]))
    print(Solution().fun(["4", "13", "5", "/", "+"]))

# TTR:
# if int, stack.append(i)
# else pop b,a
# repr(int(eval(a+i+b)))
