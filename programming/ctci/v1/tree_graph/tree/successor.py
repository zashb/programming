import unittest


class Tree_Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


def get_inorder(root):
    if root is None:
        return None
    get_inorder(root.left)
    print(root.val)
    get_inorder(root.right)


def insert(root, val):
    if root is None:
        root = Tree_Node(val)
    else:
        if val > root.val:
            if root.right is None:
                root.right = Tree_Node(val)
            else:
                insert(root.right, val)
        else:
            if root.left is None:
                root.left = Tree_Node(val)
            else:
                insert(root.left, val)


def get_io_successor(root, target):
    candidate = None
    while root:
        if root.val == target:
            if root.right is not None:
                candidate = root.right
                while candidate.left is not None:
                    candidate = candidate.left
            root = None
        elif target < root.val:
            candidate = root
            root = root.left
        else:
            root = root.right
    return candidate.val


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = Tree_Node(20)
        insert(root, 8)
        insert(root, 22)
        insert(root, 4)
        insert(root, 12)
        insert(root, 10)
        insert(root, 14)
        succ = get_io_successor(root, 14)
        print(succ)
