from bintree_class import TreeNode

class Solution:
    def maxPathSum(self, root):
        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0
            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain
            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)
            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)
        max_sum = float('-inf')
        max_gain(root)
        return max_sum

root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
expected = 42
actual = Solution().maxPathSum(root)
print(actual == expected)



# from gfg_top10.tree.TreeNode import TreeNode


# def get_max_path_sum(root):
#     # Initialize result
#     get_max_path_sum_util.res = float("-inf")
#     # Compute and return result
#     get_max_path_sum_util(root)
#     return get_max_path_sum_util.res


# def get_max_path_sum_util(root):
#     # Base Case
#     if root is None:
#         return 0
#     # l and r store maximum path sum going through left and right child of root respetively
#     l = get_max_path_sum_util(root.left)
#     r = get_max_path_sum_util(root.right)
#     # Max path for parent call of root. This path must include at most one child of root
#     max_single = max(max(l, r) + root.val, root.val)
#     # Max top represents the sum when the node under consideration is the root of the maxSum path and no ancestor of root are there in max sum path
#     max_top = max(max_single, l + r + root.val)
#     # Static variable to store the changes Store the maximum result
#     get_max_path_sum_util.res = max(get_max_path_sum_util.res, max_top)
#     return max_single


# root = TreeNode(10)
# root.left = TreeNode(2)
# root.right = TreeNode(10)
# root.left.left = TreeNode(20)
# root.left.right = TreeNode(1)
# root.right.right = TreeNode(-25)
# root.right.right.left = TreeNode(3)
# root.right.right.right = TreeNode(4)
# expected = 42
# actual = get_max_path_sum(root)
# print(expected == actual)
