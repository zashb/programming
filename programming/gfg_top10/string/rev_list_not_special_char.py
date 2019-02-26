import unittest


def reverse_list(string):
    # use stack to rev
    # if not alnum dont swap
    stack = []
    result = []
    for i in string:
        if i.isalnum():
            stack.append(i)
    for i in string:
        if i.isalnum():
            result.append(stack.pop())
        else:
            result.append(i)
    return "".join(result)


def reverse_list_2(string):
    # use l, r to swap
    string_list = list(string)
    l, r = 0, len(string_list) - 1
    while l < r:
        if not string_list[l].isalnum():
            l += 1
        elif not string_list[r].isalnum():
            r -= 1
        else:
            string_list[l], string_list[r] = string_list[r], string_list[l]
            l += 1
            r -= 1
    return "".join(string_list)


class Test(unittest.TestCase):
    def test_reverse_list(self):
        string = "a,b$c"
        expected = "c,b$a"
        actual = reverse_list(string)
        self.assertEquals(expected, actual)
        actual = reverse_list_2(string)
        self.assertEquals(expected, actual)
