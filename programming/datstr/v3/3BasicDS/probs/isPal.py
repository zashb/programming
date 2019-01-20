class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def insertAtHead(self, x):
        newNode = ListNode(x)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def isPal(self):
        # helper method to push elements into stack
        def _getStack():
            curr = self.head
            stack = []
            while curr:
                stack.append(curr.val)
                curr = curr.next
            return stack

        stack = _getStack()
        curr = self.head
        while curr:
            if curr.val == stack.pop():
                curr = curr.next
            else:
                print("not pal")
                return
        print("is Pal")


if __name__ == "__main__":
    l = Solution()
    for i in ["a", "b", "a", "c", "a", "b", "a"]:
        l.insertAtHead(i)
    print("sorted list :")
    l.printList()
    l.isPal()
