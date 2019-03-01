import unittest

from programming.ctci.v1.linked_list.linked_list import LinkedList, LinkedListNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ll1 = LinkedList()
        ll1.head = LinkedListNode(1)
        ll1.head.next = LinkedListNode(2)
        ll1.head.next.next = LinkedListNode(3)
        ll2 = LinkedList()
        ll2.head = LinkedListNode(10)
        ll2.head.next = LinkedListNode(11)
        ll2.head.next.next = ll1.head.next.next
        actual = intersect(ll1, ll2)
        print(actual)


def intersect(ll1, ll2):
    head1, head2 = ll1.head, ll2.head
    if not head1 or not head2:
        return None
    current1, current2 = head1, head2
    while current1 != current2 and (current1 or current2):
        if not current1:
            current1 = head2
        if not current2:
            current2 = head1
        if current1 == current2:
            break
        current1 = current1.next
        current2 = current2.next
    return current1 if current1 == current2 else None


if __name__ == '__main__':
    unittest.main()
