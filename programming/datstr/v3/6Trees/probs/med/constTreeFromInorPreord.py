class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(inOrder, preOrder, inStrt, inEnd):
    if (inStrt > inEnd):
        return None
    # Pich current node from Preorder traversal using preIndex and increment preIndex
    tNode = TreeNode(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    # If this node has no children then return
    if inStrt == inEnd:
        return tNode
    # Else find the index of this node in Inorder traversal
    inIndex = _search(inOrder, inStrt, inEnd, tNode.val)
    # Using index in Inorder Traversal, construct left and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
    tNode.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)
    return tNode


def _search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def _printInorder(node):
    if node is None:
        return
    _printInorder(node.left)
    print(node.val)
    _printInorder(node.right)


if __name__ == "__main__":
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    buildTree.preIndex = 0
    root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
    _printInorder(root)
