from bintree_class import TreeNode


def getTreeSize(root):
    if root is None:
        return 0
    else:
        return 1 + getTreeSize(root.left) + getTreeSize(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

expected = 5
actual = getTreeSize(root)
print(expected == actual)
