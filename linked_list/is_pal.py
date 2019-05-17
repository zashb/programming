import unittest

from ctci.v1.linked_list.linked_list import LinkedList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ll = LinkedList()
        ll.generate(10, 0, 10)
        actual = is_pal(ll)
        print(actual)


def is_pal(ll):
    ll2 = reverse_and_clone(ll)
    print(ll)
    print(ll2)
    return are_equal(ll, ll2)


def are_equal(ll, ll2):
    if len(ll) != len(ll2):
        return False
    a = ll.head
    b = ll2.head
    while a and b:
        if a.value != b.value:
            return False
        a = a.next
        b = b.next
    return not a and not b


def reverse_and_clone(ll):
    ll2 = LinkedList()
    current = ll.head
    while current:
        ll2.add_to_beginning(current.value)
        current = current.next
    return ll2


if __name__ == '__main__':
    unittest.main()
