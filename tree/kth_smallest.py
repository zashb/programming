"""
prob: find kth smallest val in BST
idea: stack
comp: O(n)
"""
from tree.bintree_class import TreeNode


def k_small(root, k):
    if not root or not k:
        return root
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right


def insert(root, val):
    node = TreeNode(val)
    if not root:
        root = node
    elif val > root.val:
        if not root.right:
            root.right = node
        else:
            insert(root.right, val)
    else:
        if not root.left:
            root.left = node
        else:
            insert(root.left, val)


root = TreeNode(3)
for i in [1, 4, 2]:
    insert(root, i)
expected = 1
actual = k_small(root, 1)
print(expected == actual)

root = TreeNode(5)
for i in [1, 4, 2, 3, 5, 6]:
    insert(root, i)
expected = 3
actual = k_small(root, 3)
print(expected == actual)
