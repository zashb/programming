def main(nums,k):
    perms = getPerms(nums)
    print(sorted(perms)[k-1])
    return

def getPerms(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break              #handles duplication
        ans = new_ans
    return ans

if __name__ == '__main__':
    n,k=3,4
    nums = list(range(1,n+1))
    main(nums,k)