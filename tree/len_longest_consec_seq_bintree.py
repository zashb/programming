"""
prob: Find the length of Longest Consecutive Path in Binary Tree. The path can be both increasing or decreasing i,e [1,2,3,4] and [4,3,2,1] are both considered valid. The path can be child-Parent-child not necessarily parent-child.
idea: 
With every node, we associate two values/variables named inr,dcr, where "inr" represents the length of the longest incrementing branch below the current node including itself, and "dcr" represents the length of the longest decrementing branch below the current node including itself.
We make use of a recursive function longestPath(node) which returns an array of the form [inr, dcr] for the calling node. 
comp: O(N)
"""


from tree.bintree_class import TreeNode
# from bintree_class import TreeNode

def len_longestConsecutive(root):
    def dfs(node, parent):
        if not node:
            return 0, 0
        li, ld = dfs(node.left, node)
        ri, rd = dfs(node.right, node)
        l[0] = max(l[0], li + rd + 1, ld + ri + 1)
        if node.val == parent.val + 1:
            return max(li, ri) + 1, 0
        if node.val == parent.val - 1:
            return 0, max(ld, rd) + 1
        return 0, 0
    l = [0]
    dfs(root, root)
    return l[0]


root = TreeNode(1, TreeNode(2), TreeNode(3))
expeted = 2
actual = len_longestConsecutive(root)
print(expeted == actual)

root = TreeNode(2, TreeNode(1), TreeNode(3))
expeted = 3
actual = len_longestConsecutive(root)
print(expeted == actual)