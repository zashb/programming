"""
is S subtree of T
Comp : O(mn) where m and n are number of nodes in given two trees.
"""
from programming.gfg_top10.tree.TreeNode import TreeNode


def is_subtree(T, S):
    if S is None:
        return True
    if T is None:
        return False
    if are_identical(T, S):
        return True
    return is_subtree(T.left, S) or is_subtree(T.right, S)


def are_identical(Troot, Sroot):
    if Troot is None and Sroot is None:
        return True
    if Troot is None or Sroot is None:
        return False
    return Troot.val == Sroot.val and are_identical(Troot.left, Sroot.left) and are_identical(Troot.right, Sroot.right)


# initializing using left, right args
# build from bottom up
rr = TreeNode(3)
r = TreeNode(3, right=rr)
llr = TreeNode(30)
ll = TreeNode(4, right=llr)
lr = TreeNode(6)
l = TreeNode(10, left=ll, right=lr)
Troot = TreeNode(26, right=r, left=l)

lr2 = TreeNode(30)
l2 = TreeNode(4, right=lr2)
r2 = TreeNode(6)
Sroot = TreeNode(10, left=l2, right=r2)
print("Is S a subtree of T : {}".format(is_subtree(Troot, Sroot)))

# T = TreeNode(26)
# T.right = TreeNode(3)
# T.right.right = TreeNode(3)
# T.left = TreeNode(10)
# T.left.left = TreeNode(4)
# T.left.left.right = TreeNode(30)
# T.left.right = TreeNode(6)
# S = TreeNode(10)
# S.right = TreeNode(6)
# S.left = TreeNode(4)
# S.left.right = TreeNode(30)
# print("Is S a subtree of T : {}".format(is_subtree(T, S)))
