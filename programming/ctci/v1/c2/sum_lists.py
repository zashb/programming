import unittest

from programming.ctci.v1.c2.linked_list import LinkedList
from programming.ctci.v1.c2.linked_list import LinkedListNode


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ll1 = LinkedList([7, 1, 6])
        ll2 = LinkedList([5, 9, 2])
        carry = 0
        sum_lists(ll1.head, ll2.head, carry)


def sum_lists(ll1, ll2, carry):
    # recursive solution, no while loop
    if not ll1 and not ll2 and not carry:
        return None
    value = carry
    if ll1:
        value += ll1.value
    if ll2:
        value += ll2.value
    result = LinkedListNode(value % 10)
    if ll1 or ll2:
        more = sum_lists(ll1.next if ll1 else None, ll2.next if ll2 else None, 1 if value >= 10 else 0)
        result.next = more
    print(result.value)
    return result


if __name__ == '__main__':
    unittest.main()
