import sys
import unittest


# https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
# https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/

# O(h)
from tree.bintree_class import TreeNode


def insert(root, new_node):
    # recursion without return
    if root is None:
        root = new_node
    else:
        if new_node.val > root.val:
            if root.right is None:
                root.right = new_node
            else:
                insert(root.right, new_node)
        else:
            if root.left is None:
                root.left = new_node
            else:
                insert(root.left, new_node)


# comp: time-O(n), space-O(1) if Function Call Stack size is not considered, otherwise O(n)
def is_bst(root):
    return is_bst_util(root, -1 * sys.maxsize, sys.maxsize)


def is_bst_util(node, minv, maxv):
    if node is None:
        return True
    if node.val < minv or node.val > maxv:
        return False
    # key steps
    util_left = is_bst_util(node.left, minv, node.val - 1)
    util_right = is_bst_util(node.right, node.val + 1, maxv)
    return util_left and util_right


def search(root, val):
    if root is None or root.val == val:
        return root
    if val > root.val:
        return search(root.right, val)
    return search(root.left, val)


def get_inorder(root):
    if root:
        get_inorder(root.left)
        print(root.val, end=",")
        get_inorder(root.right)


r = TreeNode(50)
# insert() includes root as arg
insert(r, TreeNode(30))
insert(r, TreeNode(20))
insert(r, TreeNode(40))
insert(r, TreeNode(70))
insert(r, TreeNode(60))
insert(r, TreeNode(80))
print("is bst : {}".format(is_bst(r)))
print("inorder: ")
get_inorder(r)
for i in [30, 300]:
    actual = True if search(r, i) else False
    print("search for {} : {}".format(i, actual))
