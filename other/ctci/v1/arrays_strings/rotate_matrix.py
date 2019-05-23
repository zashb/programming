import unittest

class Test(unittest.TestCase):
    """Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees"""
    data = [([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
    [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]])]
    def test_mat_rot(self):
        for case in self.data:
            actual = mat_rot(case[0])
            self.assertEqual(actual, case[1])

def mat_rot(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            top = matrix[layer][i]
            matrix[layer][i] = matrix[-i - 1][layer]
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]
            matrix[i][- layer - 1] = top
    return matrix

if __name__ == "__main__":
    unittest.main()
