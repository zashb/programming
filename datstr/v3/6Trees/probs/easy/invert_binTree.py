class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def invertBinTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                # swap left,right
                node.right, node.left = node.left, node.right
                # order not imp, append left,right to the stack
                # stack += node.left,node.right
                stack += [node.left]
                stack += [node.right]
        return root

    def preorderTraversal(self, root):
        if root:
            print(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    Solution().preorderTraversal(root)
    print("---------------------------")
    Solution().preorderTraversal(Solution().invertBinTree(root))
