class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        stack = [(root, sum)]
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right and node.val == value:
                    return True
                stack.append((node.left, value - node.val))
                stack.append((node.right, value - node.val))
            else:
                continue
        return False


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().hasPathSum(root, 6))
