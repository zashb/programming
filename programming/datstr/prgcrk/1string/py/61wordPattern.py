def main(pattern,str):
    str_split = str.split()
    # for i in [list(map(pattern.find, pattern)),list(map(str_split.index, str_split))]: print(i)
    return list(map(pattern.find, pattern)) == list(map(str_split.index, str_split))
    
if __name__ == '__main__':
    print(main(pattern = "abba", str = "dog cat cat dog"))
    print(main(pattern = "abba", str = "dog cat cat fish"))