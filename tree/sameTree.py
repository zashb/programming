from tree.bintree_class import TreeNode


def areIdenticalTrees(a, b):
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return (a.val == b.val) and areIdenticalTrees(a.left, b.left) and areIdenticalTrees(a.right, b.right)
    return False


root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

expected = True
actual = areIdenticalTrees(root1, root2)
print(expected == actual)
