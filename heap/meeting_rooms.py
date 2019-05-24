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


def printMaxActivities(arr):
    sorted_arr = sorted(arr, key=lambda x: x[1])
    s, f = [], []
    for i in sorted_arr:
        s.append(i[0])
        f.append(i[1])
    i = 0
    print(i, )
    for j in range(len(f)):
        if s[j] >= f[i]:
            print(j, )
            i = j


expected = False
actual = can_attend_all_meetings([[0, 30], [5, 10], [15, 20]])
print(expected == actual)

expected = [0, 1]
printMaxActivities([[0, 30], [5, 10], [15, 20]])
