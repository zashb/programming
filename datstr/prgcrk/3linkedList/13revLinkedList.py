class Listnode:
    def __init__(self, x):
        self.val = x
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
            print(curr.val)
            curr = curr.next

    def revlist(self, head):
        if not head:
            return
        self.revlist(head.next)
        print(head.val)


if __name__ == '__main__':
    s = Solution()
    for i in [20, 4, 15, 85]:
        s.push(i)
    print("list:")
    s.printlist()
    print("rev list:")
    s.revlist(s.head)