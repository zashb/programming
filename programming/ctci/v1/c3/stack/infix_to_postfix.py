import unittest

from programming.ctci.v1.c3.stack import StackList


def convert_infix_to_postfix(exp):
    # op_precendence = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}
    # stack = StackList()
    # output = []
    # for i in exp:
    #     # If the character is an operand, add it to output
    #     if i.isalpha():
    #         output.append(i)
    #     # If the character is an '(', push it to stack
    #     elif i == '(':
    #         stack.push(i)
    #     # If the scanned character is an ')', pop and  output from the stack until and '(' is found
    #     elif i == ')':
    #         while (not stack.is_empty(stack.stack)) and stack.stack[-1] != '(':
    #             output.append(stack.pop())
    #         if (not stack.is_empty(stack.stack)) and stack.stack[-1] != '(':
    #             return -1
    #         else:
    #             stack.pop()
    #     # An operator is encountered
    #     else:
    #         while (not stack.is_empty(stack.stack)) and op_precendence[i] <= op_precendence.setdefault(stack.stack[-1], 100):
    #             output.append(stack.pop())
    #         stack.push(i)
    # # pop all the operator from the stack
    # while not stack.is_empty(stack.stack):
    #     output.append(stack.pop())
    # return "".join(output)

    stack = StackList()
    result = []
    for i in exp:
        if i.isalpha():
            result.append(i)
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while not stack.is_empty(stack.stack) and stack.stack[-1] != "(":
                result.append(stack.pop())
            if not stack.is_empty(stack.stack) and stack.stack[-1] != "(":
                return -1
            else:
                stack.pop()
        else:
            while not stack.is_empty(stack.stack) and is_smaller(i, stack.stack):
                result.append(stack.pop())
            stack.push(i)
        while not stack.is_empty(stack.stack):
            result.append(stack.pop())
    return "".join(result)


def is_smaller(operator, stack):
    op_precedence = {"+": 0, "-": 0, "*": 1, "/": 1, "^": 2}
    if operator not in op_precedence:
        return False
    if op_precedence[operator] <= op_precedence[stack[-1]]:
        return True


class Test(unittest.TestCase):
    def test_convert_infix_to_postfix(self):
        exp = "a+b*(c^d-e)^(f+g*h)-i"
        actual = convert_infix_to_postfix(exp)
        print(actual)
