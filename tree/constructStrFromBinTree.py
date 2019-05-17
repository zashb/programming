from tree.tree_class import TreeNode


def tree2Str(root):
    if not root:
        return ""
    left = "({})".format(tree2Str(root.left)) if root.left or root.right else ""
    right = "({})".format(tree2Str(root.right)) if root.right else ""
    return "{0}{1}{2}".format(root.val, left, right)


def preorderTrav(root):
    if root:
        print(root.val)
        preorderTrav(root.left)
        preorderTrav(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

preorderTrav(root)
print("---------------------")
print(tree2Str(root))
print("---------------------")
print("---------------------")

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
preorderTrav(root)
print("---------------------")
print(tree2Str(root))
