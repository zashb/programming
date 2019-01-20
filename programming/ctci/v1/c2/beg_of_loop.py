import unittest

from programming.ctci.v1.c2.linked_list import LinkedList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ll = LinkedList()
        ll.generate(10, 0, 10)
        actual = beg_of_loop(ll)
        print(actual)


def beg_of_loop(ll):
    slow = fast = ll.head
    # meeting point -> loop size - k
    while fast and slow:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    # if no meeting point, then no loop
    if not fast or not slow:
        return None
    # Move slow to Head.
    # Keep fast at Meeting Point.
    # Each are k steps from the Loop Start.
    # If they move at the same pace, they must meet at Loop Start
    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast


if __name__ == '__main__':
    unittest.main()
