class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getTreeSize(root):
    if root is None:
        return 0
    else:
        return 1 + getTreeSize(root.left) + getTreeSize(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(getTreeSize(root))
