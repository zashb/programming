class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isValidChildSum(root):
    leftVal, rightVal = 0, 0
    if root is None or (root.left is None and root.right is None):
        return 1
    else:
        if root.left:
            leftVal = root.left.val
        if root.right:
            rightVal = root.right.val
        if root.val == leftVal + rightVal and isValidChildSum(root.left) != 0 and isValidChildSum(root.right) != 0:
            return 1
        else:
            return 0


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(2)
    print(isValidChildSum(root))
