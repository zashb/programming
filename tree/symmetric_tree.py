"""
prob: Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
Example: this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
idea: queue
comp: O(n)
"""
from collections import deque

from tree.bintree_class import TreeNode


def is_symmetric(root):
    if not root:
        return False
    queue = deque()
    queue.append(root)
    queue.append(root)
    while queue:
        t1 = queue.popleft()
        t2 = queue.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.val != t2.val:
            return False
        queue.append(t1.left)
        queue.append(t2.right)
        queue.append(t1.right)
        queue.append(t2.left)
    return True


root = TreeNode(1,
                TreeNode(2,
                         TreeNode(3),
                         TreeNode(4)),
                TreeNode(2,
                         TreeNode(4),
                         TreeNode(3)))
expected = True
actual = is_symmetric(root)
print(expected == actual)
