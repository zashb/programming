import unittest

from programming.gfg_top10.tree.TreeNode import TreeNode


def get_lca(root, n1, n2):
    if root is None:
        return None
    if n1 < root.val and n2 < root.val:
        return get_lca(root.left, n1, n2)
    if n1 > root.val and n2 > root.val:
        return get_lca(root.right, n1, n2)
    return root.val


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = TreeNode(20)
        root.left = TreeNode(8)
        root.right = TreeNode(22)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(12)
        root.left.right.left = TreeNode(10)
        root.left.right.right = TreeNode(14)
        n1 = 10
        n2 = 14
        expected = 12
        actual = get_lca(root, n1, n2)
        self.assertEqual(expected, actual)

        n1 = 14
        n2 = 8
        expected = 8
        actual = get_lca(root, n1, n2)
        self.assertEqual(expected, actual)

        n1 = 10
        n2 = 22
        expected = 20
        actual = get_lca(root, n1, n2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
