import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        set = [1, 2, 3]
        actual = get_subsets(set, 0)
        print(actual)


def get_subsets(setz, index):
    all_subsets = []
    if len(setz) == index:
        if [] not in all_subsets:
            all_subsets.append([])
    else:
        all_subsets = get_subsets(setz, index + 1)
        item = setz[index]
        more_subsets = []
        for subset in all_subsets:
            new_subset = []
            for value in subset:
                if value not in new_subset:
                    new_subset.append(value)
            new_subset.append(item)
            more_subsets.append(new_subset)
        for value in more_subsets:
            if value not in new_subset:
                all_subsets.append(value)
    return all_subsets


if __name__ == '__main__':
    unittest.main()
