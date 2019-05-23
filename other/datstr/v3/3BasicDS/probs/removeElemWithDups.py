class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "{}->{}".format(self.val, repr(self.next))


class Solution:
    def delElemWithDups(self, head):
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur is not None:
            if cur.next and cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                pre.next = cur
            else:
                pre.next = cur
                pre, cur = cur, cur.next
        return dummy.next


if __name__ == "__main__":
    head, head.next, head.next.next = ListNode(1), ListNode(2), ListNode(3)
    head.next.next.next, head.next.next.next.next = ListNode(3), ListNode(4)
    head.next.next.next.next.next, head.next.next.next.next.next.next = ListNode(4), ListNode(5)
    print(Solution().delElemWithDups(head))

    # TTR:
    # 4 pts head,dummy,curr,prev(to not lose track)
    # if cur.val==cur.next.val then extract val, and while curr.val==val:curr=curr.next; pre.next=curr
    # else pre.next=cur,cur=pre,cur.next=cur
