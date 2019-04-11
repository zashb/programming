import unittest

from ctci.v1.linked_list.linked_list import LinkedList


class Test(unittest.TestCase):
    def test_rem_dup(self):
        ll = LinkedList()
        ll.generate(100, 0, 9)
        size_before = len(ll)
        print("before : {}".format(ll))
        remove_dups(ll)
        size_after = len(ll)
        print("after : {}".format(ll))
        self.assertTrue(size_before > size_after)

    def test_remove_dup_2(self):
        ll = LinkedList()
        ll.generate(100, 0, 9)
        size_before = len(ll)
        print("before : {}".format(ll))
        remove_dup_2(ll)
        size_after = len(ll)
        print("after : {}".format(ll))
        self.assertTrue(size_before > size_after)


def remove_dups(ll):
    if ll.head is None:
        return
    current = ll.head
    seen = {current.value}
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return ll


def remove_dup_2(ll):
    if not ll:
        return None
    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


if __name__ == "__main__":
    unittest.main()
