def main(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in range(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break              #handles duplication
        ans = new_ans
    return ans

#     res =[]
#     if not nums or len(nums)==0:    return res
#     used = [True]*len(nums)
#     tmp = []
#     dfs(nums,used,tmp,res)
#     return res

# def dfs(nums,used,tmp,res):
#     if len(tmp)==len(nums):
#         res.append(tmp)
#         return
#     for i in range(len(nums)):
#         if used[i]: continue
#         if i > 0 and nums[i-1]==nums[i] and not used[i-1]:  continue
#         used[i] = True
#         tmp.append(nums[i])
#         dfs(nums,used,tmp,res)
#         used[i] = False
#         # tmp.remove(len(tmp)-1)
#         tmp = tmp[:-1]

if __name__ == '__main__':
    print(main([2,1,3]))    
    print(main([2,1,3,1]))