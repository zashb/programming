"""
prob:
idea:
comp: O(n)
"""
from ctci.v1.linked_list.linked_list import LinkedList, LinkedListNode


def has_cycle(head):
    if not head or not head.next:
        return False
    slow, fast = head, head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow, fast = slow.next, fast.next.next
    return True


ll = LinkedList()
ll.head = LinkedListNode(1)
ll.head.next = LinkedListNode(2)
ll.head.next.next = LinkedListNode(3)
ll.head.next.next = ll.head.next
expected = True
actual = has_cycle(ll.head)
print(expected == actual)
