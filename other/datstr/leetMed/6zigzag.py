def zigzag(s, r):
    rows, idx, step = [""] * r, 0, -1
    for i in s:
        rows[idx] += i
        if idx == 0 or idx == r - 1:
            step = -step
        idx = idx + step
    return "".join(rows)


print(zigzag("paypalishiring", 3))
