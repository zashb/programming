"""
prob: Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
comp: O(n)
"""


from bintree_class import TreeNode


def hasPathSum(root, sum):
    if not root:
        return False
    sum -= root.val
    if not root.left and not root.right:  # if reach a leaf
        return sum == 0
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)


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
