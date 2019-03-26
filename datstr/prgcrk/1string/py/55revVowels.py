import re

def main(s):
    vowels = re.findall('[aeiou]', s)
    return re.sub('[aeiou]', lambda x: vowels.pop(), s)

if __name__ == '__main__':
    print(main("hello"))
    print(main("leetcode"))
    print(main("elephant"))