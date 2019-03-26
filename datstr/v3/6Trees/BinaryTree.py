# from collections import deque
#
#
# class BinaryTree:
#     def __init__(self, root):
#         self.key = root
#         self.leftChild = None
#         self.rightChild = None
#
#     def insertLeft(self, newNode):
#         if self.leftChild is None:
#             self.leftChild = BinaryTree(newNode)
#         else:
#             temp = BinaryTree(newNode)
#             temp.leftChild = self.leftChild
#             self.leftChild = temp
#
#     def insertRight(self, newNode):
#         if self.rightChild is None:
#             self.rightChild = BinaryTree(newNode)
#         else:
#             temp = BinaryTree(newNode)
#             temp.rightChild = self.rightChild
#             self.rightChild = temp
#
#     def getLeftChild(self):
#         return self.leftChild
#
#     def getRightChild(self):
#         return self.rightChild
#
#     def setRootVal(self, val):
#         self.key = val
#
#     def getRootVal(self):
#         return self.key
#
#     def buildParseTree(self, exp):
#         expList = exp.split()
#         stack = deque()
#         tree = BinaryTree("")
#         stack.append(tree)
#         currTree = tree
#         for i in expList:
#             if i == "(":
#                 tree.insertLeft("")
#                 stack.append(currTree)
#                 currTree = currTree.getLeftChild()
#             elif i not in ['+', '-', '*', '/', ')']:
#                 currTree.setRootVal(int(i))
#                 parent = stack.pop()
#                 currTree = parent
#             elif i in ['+', '-', '*', '/']:
#                 currTree.setRootVal(i)
#                 currTree.insertRight('')
#                 stack.push(currTree)
#                 currTree = currTree.getRightChild()
#             elif i == ')':
#                 currTree = stack.pop()
#             else:
#                 raise ValueError
#         return tree
#
#
# if __name__ == "__main__":
#     tree = BinaryTree("a")
#     tree.insertLeft("b")
#     tree.insertRight("c")
#     print(tree.getRootVal())
#     print(tree.getLeftChild())
#     print(tree.getRightChild())
#     # print(BinaryTree().buildParseTree("( ( 10 + 5 ) * 3 )"))

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insertLeft(self, item):
        # if no left then make it left
        if self.left is None:
            self.left = BinaryTree(item)
        # if there is left, make it as left of new item and make the new item the left
        else:
            BinaryTree(item).left = self.left
            self.left = BinaryTree(item)

    def insertRight(self, item):
        if self.right is None:
            self.right = BinaryTree(item)
        else:
            BinaryTree(item).right = self.right
            self.right = BinaryTree(item)

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRoot(self, item):
        self.key = item

    def getRoot(self):
        return self.key

    def preOrder(self, root):
        if root:
            print(root.key)
            self.preOrder(root.left)
            self.preOrder(root.right)


if __name__ == "__main__":
    r = BinaryTree("a")
    r.insertLeft("b")
    r.left.insertRight("d")
    r.insertRight("c")
    r.right.insertLeft("e")
    r.right.insertRight("f")
    r.preOrder(r)
