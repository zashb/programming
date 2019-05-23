"""
prob: Write a function that takes a string as input and reverse only the vowels of a string.
idea: string lower, vowels lookup, 2ptr, if vowels swap
comp:
"""


def reverse_vowels(string):
    n = len(string)
    string = list(string.lower())
    if not string or n == 1:
        return string
    vowels = {'a', 'e', 'i', 'o', 'u'}
    left, right = 0, n - 1
    while left < right:
        if string[left] not in vowels:
            left += 1
            continue
        if string[right] not in vowels:
            right -= 1
            continue
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return "".join(string)


expected = "holle"
actual = reverse_vowels("hello")
print(expected == actual)
