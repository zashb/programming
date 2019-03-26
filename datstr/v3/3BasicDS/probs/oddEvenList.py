class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def oddEvenList(self, head):
        # if head:
        #     # given head is always odd
        #     odd = head
        #     even = evenHead = odd.next
        #     while even and even.next:
        #         odd.next = odd = even.next
        #         even.next = even = odd.next
        #     odd.next = evenHead
        #     return head

        if head:
            # initialize head as odd_head, head.next will be cur
            odd_head, cur = head, head.next
            while cur and cur.next:
                # head of even = head of odd.next
                even_head = odd_head.next
                # cur will be even, thus update head of odd.next with cur.next
                odd_head.next = cur.next
                # assign head of odd.next to head of odd
                odd_head = odd_head.next
                cur.next = odd_head.next
                odd_head.next = even_head
                cur = cur.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(11)
    head.next.next = ListNode(21)
    head.next.next.next = ListNode(51)
    head.next.next.next.next = ListNode(23)

    print(Solution().oddEvenList(head))
