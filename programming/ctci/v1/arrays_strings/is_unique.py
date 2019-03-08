import unittest


class Test(unittest.TestCase):
    """Is Unique: Implement an algorithm to determine if a array_string has all unique characters."""
    true_data = ['abcd', '1234', '']
    false_data = ['abcc', '122', '#45!@#']

    def test_unique(self):
        for i in self.true_data:
            actual = unique(i)
            self.assertTrue(actual)
        for i in self.false_data:
            actual = unique(i)
            self.assertFalse(actual)


def unique(string):
    if len(string) > 128:
        return False
    ordinal_flag_list = [False for _ in range(128)]
    for char in string:
        ord_val = ord(char)
        if ordinal_flag_list[ord_val]:
            return False
        ordinal_flag_list[ord_val] = True
    return True


if __name__ == "__main__":
    unittest.main()
