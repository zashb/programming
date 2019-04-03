"""
prob: Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water
idea: 2 ptr, visualize how to compute max area - max(Max, (right - left) * min(heights[left], heights[right]))
comp: O(n)
"""


def max_area(heights):
    n = len(heights)
    if not heights or n < 2:
        return heights
    left, right, Max = 0, n - 1, 0
    while left < right:
        Max = max(Max, (right - left) * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return Max


expected = 49
actual = max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(expected == actual)
