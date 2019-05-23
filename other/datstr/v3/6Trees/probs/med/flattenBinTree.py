class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def flattenBinTree(self,root):
        stack, result = [], []
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return result



if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().flattenBinTree(root))
