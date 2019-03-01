import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Test(unittest.TestCase):
    # same as insert
    def test_min_tree(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        root = get_min_tree(arr)
        print("inorder traversal of BST :")
        inorder(root)

    def test_insert(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        r = Node(1)
        for i in arr[1:]:
            insert(r, Node(i))
        print("inorder traversal of BST :")
        inorder(r)


def insert(root, new_node):
    if root is None:
        root = new_node
    else:
        if new_node.value > root.value:
            if root.right is None:
                root.right = new_node
            else:
                insert(root.right, new_node)
        else:
            if root.left is None:
                root.left = new_node
            else:
                insert(root.left, new_node)


def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.value, end=",")
    inorder(node.right)


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
