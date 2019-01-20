import unittest

INT_MAX = 4294967296
INT_MIN = -4294967296


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_bst(root):
    return is_bst_util(root, INT_MIN, INT_MAX)


def is_bst_util(node, minv, maxv):
    if node is None:
        return True
    if node.value < minv or node.value > maxv:
        return False
    util_left = is_bst_util(node.left, minv, node.value - 1)
    util_right = is_bst_util(node.right, node.value + 1, maxv)
    return util_left and util_right


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.left.right = Node(3)
        if is_bst(root):
            print("Is BST")
        else:
            print("Not a BST")


if __name__ == '__main__':
    unittest.main()
