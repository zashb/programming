class Solution:
    def mergeSortedArrs(self, nums1, nums2):
        for i, j in enumerate(nums1):
            if j == 0 and nums2:
                nums1[i] = nums2.pop()
        return sorted(nums1)


print(Solution().mergeSortedArrs([1, 3, 15, 0, 0, 0, 0], [2, 4, 6, 8]))
