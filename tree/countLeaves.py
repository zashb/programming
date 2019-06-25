from bintree_class import TreeNode


def countLeaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    else:
        return countLeaves(root.left) + countLeaves(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

expected = 3
actual = countLeaves(root)
print(expected == actual)
