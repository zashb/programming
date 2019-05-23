import bisect

def max(nums,k):
    res,queue = [],[]
    for i, j in enumerate(nums):
        if queue and queue[0] <= i - k: queue = queue[1:]
        while queue and nums[queue[-1]] < j:    queue.pop()
        queue.append(i)
        if i + 1 >= k:  res.append(nums[queue[0]])
    return res

def median(nums,k):
    window,medians = sorted(nums[:k]),[]
    for a, b in zip(nums, nums[k:] + [0]):
        medians.append((window[k//2] + window[~(k//2)]) // 2)
        window.remove(a)
        bisect.insort(window, b)
    return medians

if __name__ == '__main__':
    print(max(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(median(nums = [1,3,-1,-3,5,3,6,7], k = 3))