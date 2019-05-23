# A peak element is an element that is greater than its neighbors.

def main(nums):
    left,right=0,len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]: return nums[mid]
        if nums[mid]<nums[mid+1]: left=mid+1
        else:   right=mid-1
    return nums[left]

if __name__ == '__main__':
    print(main([1, 2, 3, 1]))