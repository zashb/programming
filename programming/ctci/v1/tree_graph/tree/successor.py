import unittest


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def get_successor(n):
    if n.right:
        return minv(n.right)
    p = n.parent
    while p:
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


def minv(node):
    current = node
    while current is not None:
        if current.left is None:
            break
        current = current.left
    return current


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = None
        root = insert(root, 20)
        root = insert(root, 8)
        root = insert(root, 22)
        root = insert(root, 4)
        root = insert(root, 12)
        root = insert(root, 10)
        root = insert(root, 14)
        temp = root.left.right.right
        succ = get_successor(temp)
        if succ is not None:
            print("\nInorder Successor of %d is %d " % (temp.data, succ.data))
        else:
            print("\nInorder Successor doesn't exist")


if __name__ == '__main__':
    unittest.main()
