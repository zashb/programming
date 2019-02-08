import unittest


class Test(unittest.TestCase):
    """Given two strings, write a function to check if they are
one edit (or zero edits) away"""
    true_cases = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'), ('paleabc', 'pleabc')]
    false_cases = [('pkle', 'pable'), ('pal', 'palks'), ('palks', 'pal')]

    def test_one_edit(self):
        for case in self.true_cases:
            actual = one_edit(case[0], case[1])
            self.assertTrue(actual)
            actual = one_edit_2(case[0], case[1])
            self.assertTrue(actual)
        for case in self.false_cases:
            actual = one_edit(case[0], case[1])
            self.assertFalse(actual)
            actual = one_edit_2(case[0], case[1])
            self.assertFalse(actual)


def one_edit(s1, s2):
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def one_edit_2(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    # get shorter and longer strings
    # shorter = s1 if len(s1) < len(s2) else s2
    # longer = s2 if len(s1) < len(s2) else s1
    if len(s1) < len(s2):
        shorter, longer = s1, s2
    else:
        shorter, longer = s2, s1
    shorter_idx, longer_idx = 0, 0
    found_difference = False
    while longer_idx < len(longer) and shorter_idx < len(shorter):
        if shorter[shorter_idx] != longer[longer_idx]:
            # ensure that this is first found difference
            if found_difference:
                return False
            found_difference = True
            # On replace, move shorter pointer
            if len(shorter) == len(longer):
                shorter_idx += 1
        # If matching, move shorter pointer
        else:
            shorter_idx += 1
        # Always move pointer for longer string
        longer_idx += 1
    return True


if __name__ == "__main__":
    unittest.main()
