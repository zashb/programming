from tree.tree_class import TreeNode


def getAllPaths(root):
    if not root:
        return []
    res = [str(root.val) + "->" + path for path in getAllPaths(root.left)]
    res += [str(root.val) + "->" + path for path in getAllPaths(root.right)]
    return res or [str(root.val)]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

expected = ['1->2->4->6', '1->2->5', '1->3']
actual = getAllPaths(root)
print(expected == actual)
