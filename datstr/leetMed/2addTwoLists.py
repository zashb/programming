class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution:
    def addTwoLists(self, l1, l2):
        dummy = ListNode(0)
        res = dummy
        sum = 0
        while l1 or l2:
            sum //= 10
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            res.next = ListNode(sum % 10)
            res = res.next
        if sum // 10 == 1:
            res.next = ListNode(1)
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    print(342 + 465)
    print(s.addTwoLists(l1, l2))
