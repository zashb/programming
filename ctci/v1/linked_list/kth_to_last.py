import unittest

from ctci.v1.linked_list.linked_list import LinkedList


class Test(unittest.TestCase):
    def test_ktl(self):
        ll = LinkedList()
        ll.generate(10, 0, 99)
        print("actual ll : {}".format(ll))
        k = 3
        print("{} to last element : {} ".format(k, kth_to_last(ll, k)))


def kth_to_last(ll, k):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next
    while runner:
        current = current.next
        runner = runner.next
    return current


if __name__ == "__main__":
    unittest.main()
