"""
prob:The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
idea: recursion
comp: O(m)
"""
from bintree_class import TreeNode


def merge_trees(n1, n2):
    if not n1:
        return n2
    if not n2:
        return n1
    n1.val += n2.val
    n1.left = merge_trees(n1.left, n2.left)
    n1.right = merge_trees(n1.right, n2.right)
    return n1


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


root1 = TreeNode(1,
                 TreeNode(3,
                          TreeNode(5)),
                 TreeNode(2))
root2 = TreeNode(2,
                 TreeNode(1,
                          None,
                          TreeNode(4)),
                 TreeNode(3,
                          None,
                          TreeNode(7)))
actual = merge_trees(root1, root2)
inorder(actual)