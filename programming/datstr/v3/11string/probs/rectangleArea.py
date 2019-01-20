class Solution:
    def computeArea(self, a, b, c, d, e, f, g, h):
        # incorrect !!!
        # ar1=(c-a)*(d-a)
        # ar2=(g-e)*(h-f)
        # commonAr=c*h
        # return ar1+ar2-commonAr

        # # ar1 = (c - a) * (d - a)
        # # ar2 = (g - e) * (h - f)
        # # commonAr = max(min(c, g) - max(a, e), 0) * max(min(d, h) - max(b, f), 0)
        # # return ar1 + ar2 - commonAr


if __name__ == "__main__":
    print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
