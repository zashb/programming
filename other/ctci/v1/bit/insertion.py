import unittest


class Test(unittest.TestCase):
    """You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N equal to M (e.g., M becomes a substring of N located at i and starting at j)."""

    def test_set_bits(self):
        n, m = 2, 4
        i, j = 2, 4
        actual = set_bits(n, m, i, j)
        print(actual)


def set_bits(n, m, i, j):
    all_ones = 1
    left = all_ones << (j + 1)
    right = ((1 << i) - 1)
    mask = left | right
    mask_n = n & mask
    shift_m = m << i
    return mask_n | shift_m


if __name__ == "__main__":
    unittest.main()
