"""
prob: construct bin tree from io and postorder
example: For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
comp: O(N)
"""

from tree.bintree_class import TreeNode
# from bintree_class import TreeNode


def construct_bintree(io, po):
    idx_map = {val:idx for idx, val in enumerate(io)}
    def helper(in_left, in_right):
        if in_left > in_right:
            return None
        # pick up the last element as a root
        val = po.pop()
        root = TreeNode(val)
        # root splits io into left and right
        index = idx_map[val]
        root.right = helper(index + 1, in_right)
        root.left = helper(in_left, index - 1)
        return root
    return helper(0, len(io) - 1)


def io(root):
    if root:
        io(root.left)
        print(root.val, ",")
        io(root.right)


actual = construct_bintree([9,3,15,20,7], [9,15,7,20,3])
io(actual)
