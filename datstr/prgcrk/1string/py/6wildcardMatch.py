def main(s,p):
    if len(p)-p.count('*')>len(s):  return False
    dp = [True]+[False]*len(s)
    for i in p:
        if i != '*':
            for j in reversed(range(len(s))):   dp[j+1] = dp[j] and (i == s[j] or i == '?')
        else:
            for j in range(1, len(s)+1):    dp[j] = dp[j-1] or dp[j]
        dp[0] = dp[0] and i == '*'
    return dp[-1]

if __name__ == '__main__':
    print(main("aa","a"))
    print(main("aa","aa"))
    print(main("aa","a*"))
    print(main("aa","?*"))
