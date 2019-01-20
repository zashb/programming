import unittest


class Test(unittest.TestCase):
    """String Compression: Implement a method to perform basic string compression using the counts of repeated characters"""
    test_cases = [('aabcccccaaa', 'a2b1c5a3'), ('abcdef', 'abcdef')]

    def test_sc(self):
        for case in self.test_cases:
            actual = sc(case[0])
            self.assertEqual(actual, case[1])
            actual = string_compression_2(case[0])
            self.assertEqual(actual, case[1])


def sc(raw_string):
    compressed = []
    counter = 0
    for i in range(len(raw_string)):
        if i != 0 and raw_string[i] != raw_string[i - 1]:
            compressed.append(raw_string[i - 1] + str(counter))
            counter = 0
        counter += 1
    compressed.append(raw_string[-1] + str(counter))
    return min(raw_string, "".join(compressed), key=len)


def string_compression_2(string):
    compressed = ""
    count_consecutive = 0
    for i in range(len(string)):
        count_consecutive += 1
        # if next character is different than current or if it is the last char append this char to result
        if string[i] != string[i + 1] or i + 1 >= len(string):
            compressed += string[i]
            compressed += str(count_consecutive)
            count_consecutive = 0
    return compressed if len(compressed) < len(string) else string


if __name__ == "__main__":
    unittest.main()
