import os

def main(strs):
    return os.path.commonprefix(strs)   

    # if not strs:   return ""
    # zip_strs=list(zip(*strs))
    # print(zip_strs)
    # for i in range(len(zip_strs)):
    #     if len(set(zip_strs[i])) > 1:  return strs[0][:i]
    # else:   return min(strs)

if __name__ == '__main__':
    print(main(["hello","he","hell"]))