from gfg_top10.tree.TreeNode import TreeNode


def get_max_path_sum(root):
    # Initialize result
    get_max_path_sum_util.res = float("-inf")
    # Compute and return result
    get_max_path_sum_util(root)
    return get_max_path_sum_util.res


def get_max_path_sum_util(root):
    # Base Case
    if root is None:
        return 0
    # l and r store maximum path sum going through left and right child of root respetively
    l = get_max_path_sum_util(root.left)
    r = get_max_path_sum_util(root.right)
    # Max path for parent call of root. This path must include at most one child of root
    max_single = max(max(l, r) + root.val, root.val)
    # Max top represents the sum when the node under consideration is the root of the maxSum path and no ancestor of root are there in max sum path
    max_top = max(max_single, l + r + root.val)
    # Static variable to store the changes Store the maximum result
    get_max_path_sum_util.res = max(get_max_path_sum_util.res, max_top)
    return max_single


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)
expected = 42
actual = get_max_path_sum(root)
print(expected == actual)
