"""
prob: Given an n-ary tree, return the postorder traversal of its nodes' values.
idea: BFS
comp: O(n)
"""
from tree.narytree_class import NaryTreeNode


def bfs_postorder(root):
    if not root:
        return []
    stack, output = [root], []
    while stack:
        root = stack.pop()
        if root:
            output.append(root.val)
        if root.children:
            stack.extend(root.children)
    return output[::-1]


def bfs_preorder(root):
    if not root:
        return []
    stack, output = [root], []
    while stack:
        root = stack.pop()
        if root:
            output.append(root.val)
        if root.children:
            stack.extend(root.children[::-1])
    return output


root = NaryTreeNode(1,
                    [NaryTreeNode(3,
                                  [NaryTreeNode(5), NaryTreeNode(6)]),
                     NaryTreeNode(2),
                     NaryTreeNode(4)])

print(bfs_postorder(root))
print(bfs_preorder(root))
