import itertools
import time


def threeSumClosest(l, t):
    c = itertools.combinations(l, 3)
    s = [sum(i) for i in c]
    d = {abs(i - t): i for i in s}
    return d[min(d)]


start_time = time.time()
print(threeSumClosest([-1, 2, 1, -4], 1))
r1 = time.time() - start_time


def threeSumClosest_2(l, t):
    l.sort()
    r = l[0] + l[1] + l[2]
    for i in range(len(l) - 2):
        j, k = i + 1, len(l) - 1
        while j < k:
            s = l[i] + l[j] + l[k]
            if s == t:
                return s
            if abs(s - t) < abs(r - t):
                r = s
            if s < t:
                j += 1
            else:
                k -= 1
    return r


start_time = time.time()
print(threeSumClosest_2([-1, 2, 1, -4], 1))
r2 = time.time() - start_time

print("r1 == r2: {}".format(r1 == r2))
