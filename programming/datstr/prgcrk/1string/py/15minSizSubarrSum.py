# return minimum size of subarray that can produce the given sum

def minSizSubarrSum(nums, target):
    if not nums or len(nums)==0:  return 0
    i,j,_sum,_min=0,0,0,99999
    while j<len(nums):
        _sum+=nums[j]
        j+=1
        while _sum>=target:
            _min=min(_min,j-i)
            _sum-=nums[i]
            i+=1
    return 0 if _min==99999 else _min
    
if __name__ == '__main__':
    print(minSizSubarrSum([2, 3, 1, 2, 4, 3], 7))
