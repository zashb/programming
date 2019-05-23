# refer to /Users/bhargavayyagari/github/programming/ctci/v1/stack_queue/stack/balanced_parenthesis.py
def validParen(s):
    d = {"(": ")", "{": "}", "[": "]"}
    stk = []
    for i in s:
        if i in d:  stk.append(i)
        elif stk and d[stk[-1]] == i: stk.pop()
        else:   return False
    return not stk

if __name__ == '__main__':
    print(validParen("()[]{}"))
    print(validParen("([)]"))

# algo
# if open: stk.append elif close: if stk and map[stk[-1]]==i: pop() else: False
# return not stk