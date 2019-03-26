class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def hasPathSum(root, s):
    if root is None:
        return 0
    else:
        res = 0
        subSum = s - root.val
        if root.left is None and root.right is None and subSum == 0:
            return 1
        if root.left:
            res = res or hasPathSum(root.left, subSum)
        if root.right:
            res = res or hasPathSum(root.right, subSum)
        return res


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(2)
    s = 21
    print(hasPathSum(root, s))
