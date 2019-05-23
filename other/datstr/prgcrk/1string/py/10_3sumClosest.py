def _3sumClosest(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    if result==target:  return result
    for i in range(len(nums) - 2):
        j, k = i+1, len(nums) - 1
        while j < k:
            _sum = nums[i] + nums[j] + nums[k]
            if _sum == target:   return _sum
            if abs(_sum - target) < abs(result - target):    result = _sum
            if _sum < target:    j += 1
            elif _sum > target:  k -= 1
    return result


if __name__ == '__main__':
    print(_3sumClosest([-1, 2, 1, -4], 1)) 

# algo
# 3 pts: i:loop,j:i+1,k=len(l)-1
# while j<k: if s<t:j+=1 else: k-=1
