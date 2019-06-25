"""
prob: The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
example:Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
idea: stack
comp: O(n)
"""
from bintree_class import TreeNode


def get_max_depth(root):
    stack = []
    if root:
        stack.append((1, root))
    max_depth = 0
    while stack:
        curr_depth, root = stack.pop()
        if root:
            max_depth = max(max_depth, curr_depth)
            stack.append((curr_depth + 1, root.left))
            stack.append((curr_depth + 1, root.right))
    return max_depth


root = TreeNode(3,
                TreeNode(9),
                TreeNode(20,
                         TreeNode(15),
                         TreeNode(7)))
expected = 3
actual = get_max_depth(root)
print(expected == actual)
