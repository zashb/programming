"""
prob: all paths from root
idea: recursion
comp: O(n)
"""


from bintree_class import TreeNode


class Solution():
    def get_all_paths(self, root):
        def get_paths_util(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    get_paths_util(root.left, path)
                    get_paths_util(root.right, path)
        paths = [] # external / global variable
        get_paths_util(root, '')
        return paths



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(6)

expected = ['1->2->4->6', '1->2->5', '1->3']
actual = Solution().get_all_paths(root)
print(expected == actual)

# def getAllPaths(root):
#     if not root:
#         return []
#     res = [str(root.val) + "->" + path for path in getAllPaths(root.left)]
#     res += [str(root.val) + "->" + path for path in getAllPaths(root.right)]
#     return res or [str(root.val)]
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.left.left.left = TreeNode(6)

# expected = ['1->2->4->6', '1->2->5', '1->3']
# actual = getAllPaths(root)
# print(expected == actual)
