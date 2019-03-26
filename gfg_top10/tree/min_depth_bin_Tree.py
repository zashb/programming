import unittest

from programming.gfg_top10.tree.TreeNode import TreeNode


# Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from root node down to the nearest leaf node

def get_min_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is None:
        get_min_height(root.right) + 1
    if root.right is None:
        get_min_height(root.left) + 1
    return min(get_min_height(root.left), get_min_height(root.right)) + 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        expected = 2
        actual = get_min_height(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
