class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        # make mid val as root
        root = TreeNode(nums[mid])
        # all elems before mid will be in left
        root.left = self.sortedArrayToBST(nums[:mid])
        # all elems after mid will be in right
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
    def preorder(self,root):
        result,stack=[],[]
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return result

if __name__ == "__main__":
    nums = [1,11,21,31,41,51]
    root = Solution().sortedArrayToBST(nums)
    print(Solution().preorder(root))