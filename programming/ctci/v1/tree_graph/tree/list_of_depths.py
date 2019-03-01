import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def list_of_depths(root):
    if not root:
        return None
    depths = []
    q = [root]
    while q:
        parents = q
        depths.append(q)
        q = []
        for parent in parents:
            if parent.left:
                q.append(parent.left)
            if parent.right:
                q.append(parent.right)
    return depths


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        depths = list_of_depths(root)
        for depth, list_nodes in enumerate(depths):
            print('Depth', depth, end=': ')
            for n in list_nodes:
                print(n.data, end=' -> ')
            print('end')


if __name__ == '__main__':
    unittest.main()
