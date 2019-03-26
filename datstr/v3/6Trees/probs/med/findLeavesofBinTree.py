class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        if not root:
            return []
        kids = list(map(self.findLeaves, (root.left, root.right)))
        return list(map(lambda l, r: (l or []) + (r or []), *kids)) + [[root.val]]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().findLeaves(root))
