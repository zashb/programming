class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def nthNodeFromBeg(self, n):
        curr, count = self.head, 0
        while curr:
            if count == n:
                return curr.val
            count += 1
            curr = curr.next
        return "{} is greater than #nodes in the list".format(n)


if __name__ == "__main__":
    s = Solution()
    s.insertAtBeg(1)
    s.insertAtBeg(4)
    s.insertAtBeg(1)
    s.insertAtBeg(12)
    s.insertAtBeg(1)
    print("list:")
    s.printList()
    n = 3
    print("{} node from beg:".format(n))
    print(s.nthNodeFromBeg(n-1))

    # TTR:
    # 1ptr,1var
    # if count==n ret curr.val else curr=curr.next,count+=1
