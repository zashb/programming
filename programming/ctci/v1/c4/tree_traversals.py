import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def get_level_order(root):
    level_count = height(root)
    for i in range(1, level_count + 1):
        print_level(root, i)


def print_level(root, level):
    if root is None:
        return None
    if level == 1:
        print(root.value),
    else:
        print_level(root.left, level - 1)
        print_level(root.right, level - 1)


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def get_level_order_efficient(root):
    if root is None:
        return None
    queue = [root]
    while queue:
        print(queue[0].value),
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def get_inorder(root):
    if root:
        get_inorder(root.left)
        print(root.value),
        get_inorder(root.right)


def get_preorder(root):
    if root:
        print(root.value),
        get_preorder(root.left)
        get_preorder(root.right)


def get_postorder(root):
    if root:
        get_postorder(root.left)
        get_postorder(root.right)
        print(root.value),


class Test(unittest.TestCase):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    def test_level_order(self):
        print("\n level order")
        get_level_order(self.root)

    def test_level_order_efficient(self):
        print("\n level order efficient")
        get_level_order_efficient(self.root)

    def test_inorder(self):
        print("\n inorder")
        get_inorder(self.root)

    def test_preorder(self):
        print("\n preorder")
        get_preorder(self.root)

    def test_postorder(self):
        print("\n postorder")
        get_postorder(self.root)
