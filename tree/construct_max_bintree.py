"""
prob: Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
comp: O(n2)
"""


from bintree_class import TreeNode
# from bintree_class import TreeNode

def constructMaximumBinaryTree(nums):
    def maxTree(nums):
        idx=nums.index(max(nums))
        node = TreeNode(nums[idx])
        if len(nums[idx+1:]) > 0:
            node.right = maxTree(nums[idx+1:])
        if len(nums[:idx]) > 0:
            node.left = maxTree(nums[:idx])
        return node
    return maxTree(nums)


def io(root):
    if root:
        io(root.left)
        print(root.val, ",")
        io(root.right)


actual = constructMaximumBinaryTree([3,2,1,6,0,5])
io(actual)