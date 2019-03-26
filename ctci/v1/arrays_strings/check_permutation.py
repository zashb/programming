import unittest


class Test(unittest.TestCase):
    """Given two strings, write a method to decide if one is a permutation of the other"""
    true_data = [('abcd', 'dabc'), ('1234', '4231'), ('a1b2c3', '3c2b1a')]
    false_data = [('abcd', 'abcd2'), ('1234', '12334'), ('a1a2a3', 'abcde'), ('ab2c', 'acbc')]

    def test_check_permutation(self):
        for case in self.true_data:
            actual = check_permutation(case[0], case[1])
            self.assertTrue(actual)
            actual = check_permutation_2(case[0], case[1])
            self.assertTrue(actual)
        for case in self.false_data:
            actual = check_permutation(case[0], case[1])
            self.assertFalse(actual)
            actual = check_permutation_2(case[0], case[1])
            self.assertFalse(actual)


def check_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    counter = {}
    for char in string1:
        if char not in counter:
            counter[char] = 1
        else:
            counter[char] += 1
    for char in string2:
        if char not in counter:
            return False
        if counter[char] == 0:
            return False
        counter[char] -= 1
    return True


def check_permutation_2(string1, string2):
    if len(string1) != len(string2):
        return False
    letters = [0] * 128
    for char in string1:
        letters[ord(char)] += 1
    for char in string2:
        letters[ord(char)] -= 1
        if letters[ord(char)] < 0:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
