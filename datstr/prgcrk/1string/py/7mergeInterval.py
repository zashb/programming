import unittest


def merge_intervals(interval_list):
    interval_list.sort(key=lambda x: x[0])
    result = []
    # init s, e
    s, e = interval_list[0][0], interval_list[0][1]
    for i in interval_list:
        if i[0] <= e:
            # update e not s
            e = max(e, i[1])
        else:
            result.append((s, e))
            # reset s, e
            s, e = i[0], i[1]
    # adding the last element
    result.append(interval_list[-1])
    return result


class Test(unittest.TestCase):
    def test_merge_intervals(self):
        i_list = [(1, 3), (2, 6), (8, 10), (15, 18)]
        expected = [(1, 6), (8, 10), (15, 18)]
        actual = merge_intervals(i_list)
        self.assertEqual(expected, actual)
