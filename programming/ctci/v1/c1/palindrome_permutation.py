import unittest


class Test(unittest.TestCase):
    """Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome"""
    data_true = ['Tact Coa', 'jhsabckuj ahjsbckj', 'azAZ']
    data_false = ['So patient a nurse to nurse a patient so', 'random', 'not a palindrome']

    def test_pal_per(self):
        for case in self.data_true:
            actual = pal_per(case)
            self.assertTrue(actual)
        for case in self.data_false:
            actual = pal_per(case)
            self.assertFalse(actual)


def pal_per(string):
    """to be a permutation of a palindrome, a string can have no more than one character that is odd"""
    table = [0 for _ in range(ord('z') - ord('a') + 1)]
    counter_odd = 0
    string_lower = string.lower()
    for char in string_lower:
        table_idx = -1
        if ord('a') <= ord(char) <= ord('z'):
            table_idx = ord(char) - ord('a')
        if table_idx != -1:
            table[table_idx] += 1
            if table[table_idx] % 2 == 1:
                counter_odd += 1
            else:
                counter_odd -= 1
    return counter_odd <= 1


if __name__ == "__main__":
    unittest.main()
