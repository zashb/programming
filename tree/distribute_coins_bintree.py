"""
prob: Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.
In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)
Return the number of moves required to make every node have exactly one coin.
idea: DFS
comp: O(N), n=#nodes
"""


from tree.bintree_class import TreeNode
# from bintree_class import TreeNode



def distributeCoins(root, pre=None):
    if not root: 
        return 0
    res = distributeCoins(root.left, root) + distributeCoins(root.right, root)
    if pre: 
        pre.val += root.val - 1
    return res + abs(root.val - 1)


root = TreeNode(3, TreeNode(0), TreeNode(0))
expected = 2
actual = distributeCoins(root)
print(expected == actual)