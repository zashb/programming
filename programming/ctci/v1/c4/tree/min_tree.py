import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Test(unittest.TestCase):
    def test_min_tree(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = get_min_tree(arr)
        print("preorder traversal of BST : {}".format(preorder(root)))


def preorder(node):
    if not node:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)


def get_min_tree(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = get_min_tree(arr[:mid])
    root.right = get_min_tree(arr[mid + 1:])
    return root


if __name__ == "__main__":
    unittest.main()
