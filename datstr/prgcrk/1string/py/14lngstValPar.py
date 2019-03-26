def lngstValPar(s):
    count = 0
    for i in range(len(s)-1):
        if s[i]+s[i+1]=="()":
            s.replace("()","")
            count += 2
    return count

    # dp, stack = [0] * (len(s) + 1), []
    # for i in range(len(s)):
    #     if s[i] == '(': stack.append(i)
    #     elif stack:
    #         p = stack.pop()
    #         dp[i + 1] = dp[p] + i - p + 1
    # # print(dp)
    # return max(dp)


if __name__ == '__main__':
    print(lngstValPar("(()"))
    print(lngstValPar(")()())"))


# note:
# let dp[i] is the number of longest valid Parentheses ended with the i - 1 position of s, then we have the following relationship:
# dp[i + 1] = dp[p] + i - p + 1 where p is the position of '(' which can matches current ')' in the stack.
