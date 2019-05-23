def revPolNot(e):
    stack = []
    for i in e.split(' '):
        if i in "+-*/":
            op1,op2=stack.pop(),stack.pop()
            d={"-":op2-op1,"+":op2+op1,"*":op2*op1,"/":op2/op1}
            if i in d:    stack.append(d[i])
            # result = stack.append(eval(str(op2) + val + str(op1)))
        else:   stack.append(float(i))
    return stack.pop()

if __name__ == '__main__':
    print(revPolNot("2 1 + 3 *"))

# algo
# if opr pop() twice
# eval(b,opr,a)