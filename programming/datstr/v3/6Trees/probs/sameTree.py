class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     # Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
#     def isSameTree(self,root1,root2):
#         if root1 and root2:
#             cond1 = root1.val == root2.val
#             cond2 = self.isSameTree(root1.left,root2.left)
#             cond3 = self.isSameTree(root1.right,root2.right)
#             return cond1 and cond2 and cond3
#         return root1 is root2
#
# if __name__ == "__main__":
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.left.left = TreeNode(3)
#     root.left.right = TreeNode(4)
#     root.right = TreeNode(5)
#     root.right.right = TreeNode(6)
#     root1 = TreeNode(1)
#     root1.left = TreeNode(2)
#     root1.left.left = TreeNode(3)
#     root1.left.right = TreeNode(4)
#     root1.right = TreeNode(5)
#     root1.right.right = TreeNode(16)
#     print(Solution().isSameTree(root,root1))

def areIdenticalTrees(a, b):
    if a is None and b is None:
        return True
    if a is not None and b is not None:
        return ((a.val == b.val) and areIdenticalTrees(a.left, b.left) and areIdenticalTrees(a.right, b.right))
    return False


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    if areIdenticalTrees(root1, root2):
        print("Both trees are identical")
    else:
        print("Trees are not identical")
