# exec(open(r"C:\Users\sg0222350\My Stuff\learn\python\dataStruct\v3\6Trees\BinaryTree.py").read())

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

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.key)
            self.inOrder(root.right)

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRoot(self, item):
        self.key = item

    def buildParsetree(self, exp):
        expList = exp.split()
        expStack = []
        expTree = BinaryTree("")
        expStack.append(expTree)
        currTree = expTree
        for i in expList:
            if i == "(":
                currTree.insertLeft("")
                expStack.append(currTree)
                currTree = currTree.getLeft()
            elif i not in "+-*/)":
                currTree.setRoot(int(i))
                parent = expStack.pop()
                currTree = parent
            elif i in "+-*/":
                currTree.setRoot(i)
                currTree.insertRight("")
                expStack.append(currTree)
                currTree = currTree.getRight()
            elif i == ")":
                currTree = expStack.pop()
            else:
                raise ValueError
        return expTree


if __name__ == "__main__":
    b = BinaryTree("")
    b.inOrder(b.buildParsetree("( ( 10 + 5 ) * 3 )"))
