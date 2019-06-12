from tree.bintree_class import TreeNode


def hasPathSum(root, s):
    if root is None:
        return 0
    else:
        res = False
        subSum = s - root.val
        if root.left is None and root.right is None and subSum == 0:
            return True
        if root.left:
            res = res or hasPathSum(root.left, subSum)
        if root.right:
            res = res or hasPathSum(root.right, subSum)
        return res


root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.right = TreeNode(5)
root.left.left = TreeNode(3)
root.right.left = TreeNode(2)
s = 21

expected = True
actual = hasPathSum(root, s)
print(expected == actual)
