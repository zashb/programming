# def bulls_cows(secret, guess):
#     bull_count, cow_count = 0, 0
#     n = len(secret)
#     for i in range(n):
#         if secret[i] == guess[i]:
#             bull_count = bull_count + 1
#     for i in guess:
#         if i in secret and guess.index(i) != secret.index(i):
#             cow_count = cow_count + 1
#     return "{}A{}B".format(bull_count, cow_count)
#
#
# secret, guess = "1807", "7810"
# expected = "1A3B"
# actual = bulls_cows(secret, guess)
# print(expected == actual)

def bullsCows(secret, guess):
    bc, cc = 0, 0
    ord_flag = [0] * 126
    for i in range(len(secret)):
        s, g = secret[i], guess[i]
        if s == g:
            bc += 1
        else:
            ord_s, ord_g = ord(s), ord(g)
            # the opposite of base condition
            if ord_flag[ord_s] < 0:
                cc += 1
            if ord_flag[ord_g] > 0:
                cc += 1
            ord_flag[ord_s] = ord_flag[ord_s] + 1
            ord_flag[ord_g] = ord_flag[ord_g] - 1
    return "{}A{}B".format(bc, cc)


if __name__ == "__main__":
    secret = "1807"
    guess = "7810"
    expected = "1A3B"
    actual = bullsCows(secret, guess)
    print(expected == actual)
    secret = "ABC"
    guess = "BDC"
    expected = "1A1B"
    actual = bullsCows(secret, guess)
    print(expected == actual)
