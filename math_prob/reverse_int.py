def reverse_int(num):
    res, num_abs = 0, abs(num)
    while num_abs != 0:
        tail = num_abs % 10
        res = res * 10 + tail
        num_abs //= 10
    return res if num > 0 else -res


expected = 321
actual = reverse_int(123)
print(expected == actual)

expected = -321
actual = reverse_int(-1230)
print(expected == actual)

expected = 0
actual = reverse_int(00)
print(expected == actual)
