import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        strings = ["abed", "later", "bead", "alert", "altered", "bade", "alter", "alerted"]
        actual = sorted_anagrams(strings)
        print(actual)


def sorted_anagrams(strings):
    anagrams = set_anagrams(strings)
    index = 0
    for k, v in anagrams.items():
        for value in anagrams[k]:
            strings[index] = value
            index += 1
    return strings


def set_anagrams(strings):
    anagrams = {}
    for i in strings:
        word = "".join(sorted(i.lower()))
        # setdefault(key[, default])
        # If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
        anagrams.setdefault(word, []).append(i)
    return anagrams


if __name__ == '__main__':
    unittest.main()
