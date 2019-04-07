"""
prob: Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

For example,
Given [ [0, 30], [5, 10], [15, 20] ],
return false.
idea:
comp:
"""


def can_attend_all_meetings(arr):
    arr.sort(key=lambda x: x[0] - x[1])
    n = len(arr)
    for i in range(n):
        if arr[i][1] > arr[i + 1][0]:
            return False
    return True


expected = False
actual = can_attend_all_meetings([[0, 30], [5, 10], [15, 20]])
print(expected == actual)
