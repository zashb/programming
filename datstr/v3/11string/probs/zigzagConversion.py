class Solution:
    def zigzagConversion(self, s, nRows):
        # r1, r2, r3 = [], [], []
        #
        # curr = 0
        # while curr < len(s) - 1:
        #     r1.append(s[curr])
        #     curr += 1
        #     r2.append(s[curr])
        #     curr += 1
        #     if curr < len(s) - 1:
        #         r3.append(s[curr])
        #         curr += 1
        #     else:
        #         break
        #     r2.append(s[curr])
        #     curr += 1
        # return "".join(r1 + r2 + r3)


        step = (nRows == 1) - 1  # 0 or -1
        # step = -1
        rows, idx = [''] * nRows, 0
        for c in s:
            rows[idx] += c
            # if idx == 0 or idx == nRows - 1:
            if idx in [0, nRows - 1]:
                step = -step  # change direction
            idx += step
        return ''.join(rows)


if __name__ == "__main__":
    print(Solution().zigzagConversion("PAYPALISHIRING", 3))

    # TTR:
    # loop through inp str not lists
    # 3 vars - rows,idx,step=[""]*nRows,0,(nRows==1)-1
