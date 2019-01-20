def main(path):
    dirs = [i for i in path.split("/") if i not in [".",""]]
    stack = []
    for i in dirs:
        if i == "..":   
            if stack:   stack.pop()
        else:   stack.append(i)
    return "/" + "/".join(stack)

if __name__ == '__main__':
    print(main("/home/"))
    print(main("/a/./b/../../c/"))