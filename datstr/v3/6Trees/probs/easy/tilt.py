class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def getTilt(self, root):
        self.res = 0

        # sums all subnodes differences and their parent node upto the node
        def _sum(node):
            if not node:
                return 0
            left, right = _sum(node.left), _sum(node.right)
            # abs diff bwn left and right
            self.res += abs(left - right)
            # sum left,right,node
            return left + right + node.val

        _sum(root)
        return self.res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    print(Solution().getTilt(root))
