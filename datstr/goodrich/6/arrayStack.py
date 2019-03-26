class ArrayStack:
    # initialize an empty list
    def __init__(self):
        self._data = []

    # return len of list
    def __len__(self):
        return len(self._data)

    # return if list is empty
    def is_empty(self):
        return len(self._data) == 0

    # add elem at top of list
    def push(self, item):
        self._data.append(item)

    # return top elem
    def top(self):
        if self.is_empty():
            raise Empty("stack is empty")
        return self._data[-1]

    # pop top elem
    def pop(self,index=-1):
        if self.is_empty():
            raise Empty("no elems to pop")
        return self._data.pop(index)


class Empty(Exception):
    pass




if __name__ == "__main__":
    a = ArrayStack()
    for i in range(11,16):
        a.push(i)
    print(a.__len__())
    print(a.pop(2))
    print(a.__len__())
    print(a.top())

    def reverse_file(filename):
        a = ArrayStack()
        original = open(filename)
        for line in original:
            b = line.rstrip("\n")
            a.push(b)
        original.close()
        output = open(filename,"w")
        while not a.is_empty():
            output.write(a.pop()+"\n")
        output.close()

    reverse_file(r"C:\Users\sg0222350\My Stuff\learn\python\dataStruct\goodrich\6\1.txt")

    def matching_parenthesis(expr):
        a = ArrayStack()
        openBraces = "({["
        closeBraces = ")}]"
        for i in expr:
            # push openBrace onto stack
            if i in openBraces:
                a.push(i)
            elif i in closeBraces:
                # nothing to match
                if a.is_empty():
                    return False
                # mismatch
                if openBraces.index(a.pop()) != closeBraces.index(i):
                    return False
        # were all symbols matched
        return a.is_empty()

    for i in ["( )(( )){([( )])}","((( )(( )){([( )])}))",")(( )){([( )])}","({[])}","("]:
        print(matching_parenthesis(i))

    def matching_html(raw):
        a = ArrayStack()
        # find first "<"
        i = raw.find("<")
        while i != -1:
            # find next ">"
            j = raw.find(">", i + 1)
            # invalid tag
            if j == -1:
                return False
            # strip <>
            tag = raw[i+1:j]
            # this is opening tag
            if not tag.startswith("/"):
                a.push(tag)
            else:
                # nothing to match
                if a.is_empty():
                    return False
                # mismatch
                if tag[1:] != a.pop():
                    return False
            # find next "<"
            i = raw.find("<",j+1)
        # were all opentags matched
        return a.is_empty()

    print(matching_html("""<body><center><h1> The Little Boat </h1></center><p> The storm tossed the little boat like a cheap sneaker in an old washing machine. The three drunken fishermen were used to such treatment, of course, but not the tree salesman, who even as a stowaway now felt that he had overpaid for the voyage. </p><ol><li> Will the salesman die? </li><li> What color is the boat? </li><li> And what about Naomi? </li></ol></body>"""))




