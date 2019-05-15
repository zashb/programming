"""
prob: evaluate parse tree
idea: tree
comp: O(n) as each node is visited once
"""
from gfg_top10.tree.TreeNode import TreeNode


def evaluate_using_parse_tree(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return int(root.val)
    left_sum = evaluate_using_parse_tree(root.left)
    right_sum = evaluate_using_parse_tree(root.right)
    if root.val == "+":
        return left_sum + right_sum
    elif root.val == "-":
        return left_sum - right_sum
    elif root.val == "*":
        return left_sum * right_sum
    else:
        return left_sum / right_sum


root = TreeNode('+')
root.left = TreeNode('*')
root.left.left = TreeNode('5')
root.left.right = TreeNode('4')
root.right = TreeNode('-')
root.right.left = TreeNode('100')
root.right.right = TreeNode('20')
expected = 100
actual = evaluate_using_parse_tree(root)
print(expected == actual)

root = TreeNode('+')
root.left = TreeNode('*')
root.left.left = TreeNode('5')
root.left.right = TreeNode('4')
root.right = TreeNode('-')
root.right.left = TreeNode('100')
root.right.right = TreeNode('/')
root.right.right.left = TreeNode('20')
root.right.right.right = TreeNode('2')
expected = 110
actual = evaluate_using_parse_tree(root)
print(expected == actual)
