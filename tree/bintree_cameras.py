"""
prob: Given a binary tree, we install cameras on the nodes of the tree. 
Each camera at a node can monitor its parent, itself, and its immediate children.
Calculate the minimum number of cameras needed to monitor all nodes of the tree.
idea: greedy, dfs
comp: O(N)
"""


from tree.bintree_class import TreeNode
# from bintree_class import TreeNode

class Solution(object):
    def minCameraCover(self, root):
        self.ans = 0
        covered = set()

        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node is not covered or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans


root = TreeNode(0, 
        TreeNode(0, 
            TreeNode(0),
            TreeNode(0)))
expected = 3
actual = Solution().minCameraCover(root)
print(actual == expected)
