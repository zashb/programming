"""
prob: sum of squares of digits == 1 recursively
"""


def is_happy_num(n):
    if not n:
        return False
    Set = set()

    def get_sum(n):
        Sum = 0
        while n > 0:
            Sum += (n % 10) ** 2
            n //= 10
        return Sum

    while n not in Set:
        Set.add(n)
        n = get_sum(n)
        if n == 1:
            return True
    return False


expected = True
actual = is_happy_num(19)
print(expected == actual)

expected = False
actual = is_happy_num(29)
print(expected == actual)
