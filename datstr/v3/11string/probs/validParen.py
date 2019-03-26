class Solution:
    def isValid(self, s):
        # parDict = {"}": "{", ')': '(', ']': "["}
        # stack = []
        # for i in s:
        #     if i in parDict.values():
        #         stack.append(i)
        #     else:
        #         if not stack or stack.pop() != parDict[i]:
        #             return False
        # return True

        d = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            else:
                if not stack or stack.pop() != d[i]:
                    print("mismatch")
                    return
        print("match")
        return


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(])"))
print(Solution().isValid("[(()]"))

    # TTR:
    # dict structure
    # outer return not stack
