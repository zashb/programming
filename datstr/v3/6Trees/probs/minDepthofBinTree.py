class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node
    def minDepth(self, root):
        if not root:
            return 0
        depth = list(map(self.minDepth, (root.left, root.right)))
        return 1 + (min(depth) or max(depth))

    # The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node
    def maxDepth(self,root):
        if not root:
            return 0
        depth = list(map(self.maxDepth,(root.left,root.right)))
        return 1+max(depth)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().minDepth(root))
