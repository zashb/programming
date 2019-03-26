class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    def preorderTraversal(self, root):
        if root:
            print(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
