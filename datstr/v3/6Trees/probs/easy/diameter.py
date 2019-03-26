class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def getDiameter(self, root):
        self.best = 1

        def _depth(root):
            if not root:
                return 0
            left = _depth(root.left)
            right = _depth(root.right)
            self.best = max(self.best, left + right + 1)
            # depth of a node until the above line
            return 1 + max(left, right)

        _depth(root)
        return self.best - 1


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    # root.left.left.left = TreeNode(6)
    print(Solution().getDiameter(root))
