class Solution:
    def lenOfLongestVaPar_v1(self, s):
        count = 0
        for i, j in enumerate(s):
            if i < len(s) - 1 and s[i] + s[i + 1] == "()":
                s.replace("()", "")
                count += 2
        return count

    def lenOfLongestValPar_v2(self, s):
        strlen = len(s)
        stack = [-1]
        res = 0
        for i in range(strlen):
            # If opening bracket, push index of it
            if s[i] == "(":
                stack.append(i)
            # If closing bracket, i.e., str[i] = ')', Pop the previous opening bracket's index
            else:
                stack.pop()
                # If stack is empty. push current index as  base for next valid substring (if any)
                if len(stack)==0:
                    stack.append(i)
                # Check if this length formed with base of current valid substring is more than max  so far
                else:
                    res = max(res, i - stack[len(stack) - 1])

        return res


if __name__ == "__main__":
    print(Solution().lenOfLongestVaPar_v1("(()"))
    print(Solution().lenOfLongestVaPar_v1(")()())"))

    print(Solution().lenOfLongestValPar_v2("(()"))
    print(Solution().lenOfLongestValPar_v2(")()())"))
    print(Solution().lenOfLongestValPar_v2("(()())()"))
