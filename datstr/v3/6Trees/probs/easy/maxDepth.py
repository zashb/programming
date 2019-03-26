class BinTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    root = BinTree(1)
    root.left = BinTree(2)
    root.right = BinTree(3)
    root.left.left = BinTree(4)
    s = Solution()
    print(s.maxDepth(root))
