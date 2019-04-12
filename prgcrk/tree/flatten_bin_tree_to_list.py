"""
prob: flatten bin_tree
idea: stack
comp:
"""
from prgcrk.tree.tree_node import Tree_Node


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root


def inorder(root):
    if root:
        print(root.val)
        inorder(root.left)
        inorder(root.right)


# def flatten_bin_tree(root):
#     if not root:
#         return root
#     stack, temp = [], root
#     while temp and stack:
#         if temp.right:
#             stack.append(temp.right)
#         if temp.left:
#             temp.right = temp.left
#             temp.left = None
#         elif not stack:
#             temp.right = stack.pop()
#         temp = temp.right


root = Tree_Node(1,
                 Tree_Node(2,
                           Tree_Node(3),
                           Tree_Node(4)),
                 Tree_Node(5,
                           None,
                           Tree_Node(6)))
print("before")
inorder(root)
s = Solution()
s.flatten(root)
print("after")
inorder(root)
