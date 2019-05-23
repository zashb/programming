import unittest


class Test(unittest.TestCase):
    """Palindrome Permutation: Given a array_string, write a function to check if it is a permutation of a palindrome"""
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
    """to be a permutation of a palindrome, a array_string can have no more than one character that is odd"""
    # table = [0 for _ in range(ord('z') - ord('a') + 1)]
    # counter_odd = 0
    # string_lower = array_string.lower()
    # for char in string_lower:
    #     table_idx = -1
    #     if ord('a') <= ord(char) <= ord('z'):
    #         table_idx = ord(char) - ord('a')
    #     if table_idx != -1:
    #         table[table_idx] += 1
    #         if table[table_idx] % 2 == 1:
    #             counter_odd += 1
    #         else:
    #             counter_odd -= 1
    # return counter_odd <= 1

    ord_flag = [0] * 128
    odd_ctr = 0
    for i in string.lower():
        if i != ' ':
            ord_flag[ord(i)] += 1
            if ord_flag[ord(i)] % 2 == 1:
                odd_ctr += 1
            else:
                odd_ctr -= 1
    return odd_ctr <= 1


if __name__ == "__main__":
    unittest.main()
