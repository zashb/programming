# all possib subsets with dups
# backtracking
def main(nums):
    res = []
    backtrack(res=res, tmp=[], nums=nums, startIdx=0)
    return res

def backtrack(res, tmp, nums, startIdx):
    res.append(tmp[:])
    for i in range(startIdx, len(nums)):
        if i > startIdx and nums[i] == nums[i - 1]: continue
        tmp.append(nums[i])
        backtrack(res=res, tmp=tmp, nums=nums, startIdx=i + 1)
        tmp.pop()

if __name__ == '__main__':
    print(main([2,1,3]))    
    print(main([2,1,3,1]))