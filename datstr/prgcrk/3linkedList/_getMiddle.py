class Listnode:
    def __init__(self, x):
        self.data = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def push(self, x):
        newnode = Listnode(x)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def getMiddleElem(self):
        slowP, fastP = self.head, self.head
        while fastP and fastP.next:
            fastP = fastP.next.next
            slowP = slowP.next
        print(slowP.data)


if __name__ == "__main__":
    l = Solution()
    for i in range(5, 0, -1):
        l.push(i)
        print("list :")
        l.printlist()
        print("middle elem")
        l.getMiddleElem()
