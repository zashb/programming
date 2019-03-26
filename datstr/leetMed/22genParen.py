def genParen(n):
    l = []
    backtrack(l, "", 0, 0, n)
    return l


def backtrack(l, s, o, c, m):
    if len(s) == m * 2:
        l.append(s)
        return
    if o < m:
        backtrack(l, s + "(", o + 1, c, m)
    if c < o:
        backtrack(l, s + ")", o, c + 1, m)


if __name__ == "__main__":
    print(genParen(3))

# The idea here is to only add '(' and ')' that we know will guarantee us a solution (instead of adding 1 too many close). Once we add a '(' we will then discard it and try a ')' which can only close a valid '('. Each of these steps are recursively called.