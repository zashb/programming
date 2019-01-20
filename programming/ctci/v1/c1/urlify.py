import unittest


class Test(unittest.TestCase):
    test_cases = [(list('much ado about nothing      '), 22,
                   list('much%20ado%20about%20nothing')),
                  (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for case in self.test_cases:
            actual = urlify(case[0], case[1])
            self.assertEqual(len(case[0]), len(actual))
            self.assertEqual(actual, case[2])
            actual = urlify_2(case[0], case[1])
            self.assertEqual(len(case[0]), len(actual))
            self.assertEqual(actual, case[2])


def urlify(string, length):
    new_index = len(string)
    for i in reversed(range(length)):
        if string[i] == " ":
            string[new_index - 3:new_index] = "%20"
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1
    return string


def urlify_2(string, truelength):
    spacecount = 0
    for i in string:
        if i == " ":
            spacecount += 1
    index = truelength + spacecount * 2
    for i in range(truelength - 1, -1, -1):
        if string[i] == " ":
            string[index - 3: index] = "%20"
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    return string


if __name__ == "__main__":
    unittest.main()
