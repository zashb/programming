import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class MyTestCase(unittest.TestCase):
    def test_something(self):
        T = Node(26)
        T.right = Node(3)
        T.right.right = Node(3)
        T.left = Node(10)
        T.left.left = Node(4)
        T.left.left.right = Node(30)
        T.left.right = Node(6)
        S = Node(10)
        S.right = Node(6)
        S.left = Node(4)
        S.left.right = Node(30)
        print("Is S a subtree of T : {}".format(is_subtree(T, S)))


def is_subtree(T, S):
    if S is None:
        return True
    if T is None:
        return False
    if are_identical(T, S):
        return True
    return is_subtree(T.left, S) or is_subtree(T.right, S)


def are_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.val == root2.val and
            are_identical(root1.left, root2.left) and
            are_identical(root1.right, root2.right))


if __name__ == '__main__':
    unittest.main()
