class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def getAllPaths(self, root):
        if not root:
            return []
        res = [str(root.val) + "->" + path for path in self.getAllPaths(root.left)]
        res += [str(root.val) + "->" + path for path in self.getAllPaths(root.right)]
        return res or [str(root.val)]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    print(Solution().getAllPaths(root))
