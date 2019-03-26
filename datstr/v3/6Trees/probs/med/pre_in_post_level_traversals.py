# rem this for life :P
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    # preorder
    def preorderTraversal(self, root):
        stack, result = [], []
        while stack or root:
            if root:
                # append root.val to result
                result.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop().right
        return result

    # inorder
    def inorderTraversal(self, root):
        stack, result = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result

    # postorder
    def postorderTraversal(self, root):
        stack, result = [], []
        while stack or root:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.right
            else:
                root = stack.pop().left

        return result[::-1]

    # level order

    def levelOrder(self, root):
        stack, result = [root], []
        while stack:
            result.append([i.val for i in stack])
            temp = []
            for i in stack:
                temp.append(i.left)
                temp.append(i.right)
            stack = [i for i in temp if i]
        return [j for i in result for j in i]


class Solution2:
    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    # level order
    def _getHeight(self, node):
        if node is None:
            return 0
        else:
            lHeight = self._getHeight(node.left)
            rHeight = self._getHeight(node.right)
            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1

    def _printLevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.val)
        elif level > 1:
            self._printLevel(root.left, level - 1)
            self._printLevel(root.right, level - 1)

    def printLevelOrder(self, root):
        h = self._getHeight(root)
        for i in range(1, h + 1):
            self._printLevel(root, i)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    # root.right.left = TreeNode(3)

    # print(Solution().preorderTraversal(root))
    # print(Solution().inorderTraversal(root))
    # print(Solution().postorderTraversal(root))
    # print(Solution().levelOrder(root))

    print("preorder")
    Solution2().preorder(root)
    print("inorder")
    Solution2().inorder(root)
    print("postorder")
    Solution2().postorder(root)
    print("level order")
    Solution2().printLevelOrder(root)
