"""
list of meeting objects, return meetings to attend. fun to return subset of meetings that maximize total number of meetings. meeting objects have name and #hours they take.

Const : [(m1,2),(m2,3),(m3,2),(m4,4)], max = 8
Idea : sort, smallest to largest
Comp : O(nlogn)
"""


def max_num_meetings(arr, max_hours):
    arr.sort(key=lambda x: x[1])
    cum_time, res = 0, []
    for obj in arr:
        cum_time += obj[1]
        if cum_time < max_hours:
            res.append(obj)
        else:
            break
    return len(res)


arr = [("m1", 2), ("m2", 3), ("m3", 2), ("m4", 4)]
max_hours = 8
expected = 3
actual = max_num_meetings(arr, max_hours)
print(expected == actual)

"""
maximize hours in meetings
Const : [(m1,2),(m2,3),(m3,5),(m4,4)], max = 8
Idea : sort desc, pick from rem
comp : O(nlogn)
"""


def max_time_in_meetings(arr, max_hours):
    arr.sort(key=lambda x: x[1], reverse=True)
    res, rem_h = [], max_hours
    for meet in arr:
        if meet[1] > rem_h:
            continue
        elif rem_h > 0:
            rem_h -= meet[1]
            res.append(meet)
    return len(res)


arr = [("m1", 2), ("m2", 3), ("m3", 5), ("m4", 4)]
max_hours = 8
expected = 2
actual = max_time_in_meetings(arr, max_hours)
print(expected == actual)
