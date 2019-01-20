class BinTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def tree2Str(self, root):
        if not root:
            return ""
        left = "({})".format(self.tree2Str(root.left)) if root.left or root.right else ""
        right = "({})".format(self.tree2Str(root.right)) if root.right else ""
        return "{0}{1}{2}".format(root.val, left, right)

    def preorderTrav(self, root):
        if root:
            print(root.val)
            self.preorderTrav(root.left)
            self.preorderTrav(root.right)


if __name__ == "__main__":
    root = BinTree(1)
    root.left = BinTree(2)
    root.right = BinTree(3)
    root.left.left = BinTree(4)
    s = Solution()
    s.preorderTrav(root)
    print("---------------------")
    print(s.tree2Str(root))
    print("---------------------")
    print("---------------------")
    root = BinTree(1)
    root.left = BinTree(2)
    root.right = BinTree(3)
    root.left.right = BinTree(4)
    s = Solution()
    s.preorderTrav(root)
    print("---------------------")
    print(s.tree2Str(root))
