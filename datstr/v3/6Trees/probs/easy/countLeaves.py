class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(countLeaves(root))
