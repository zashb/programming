import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        set = [1, 2, 3]
        actual = get_subsets(set, 0)
        print(actual)

    def test_subsets2(self):
        nums = [1, 2, 3]
        nums = [2, 1, 3, 1]
        actual = get_subsets2(nums)
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


# ignore this implementation. refer to /Users/bhargavayyagari/github/programming/datstr/prgcrk/10math/4_5subsets.py
def get_subsets2(nums):
    res = []
    backtrack(nums, res, [], 0)
    return res


def backtrack(nums, res, temp, start):
    res.append(temp)
    for i in range(start, len(nums)):
        if nums[i] not in temp:
            # we use + to obtain return value
            backtrack(nums, res, temp + [nums[i]], i + 1)


if __name__ == '__main__':
    unittest.main()
