def main(s):
    # def isvalid(s):
    #     s = filter('()'.count, s)
    #     while '()' in s:
    #         s = s.replace('()', '')
    #     return not s
    # level = {s}
    # while True:
    #     valid = (filter(isvalid, level))
    #     if valid:
    #         return valid
    #     level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

    level = {s}
    while True:
        valid = []
        for s in level:
            try:
                eval('0,' + filter('()'.count, s).replace(')', '),'))
                valid.append(s)
            except: pass
        if valid:   return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

if __name__ == '__main__':
    print(main("()())()"))
    print(main("(a)())()"))
    print(main(")("))