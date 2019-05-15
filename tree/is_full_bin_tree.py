from tree.tree_class import TreeNode


def is_full_bt(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left is not None and root.right is not None:
        return is_full_bt(root.left) and is_full_bt(root.right)
    return False


root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.left.right = TreeNode(40)
root.left.left = TreeNode(50)
root.right.left = TreeNode(60)
root.right.right = TreeNode(70)
root.left.left.left = TreeNode(80)
root.left.left.right = TreeNode(90)
root.left.right.left = TreeNode(80)
root.left.right.right = TreeNode(90)
root.right.left.left = TreeNode(80)
root.right.left.right = TreeNode(90)
root.right.right.left = TreeNode(80)
root.right.right.right = TreeNode(90)
expected = True
actual = is_full_bt(root)
print(expected == actual)
