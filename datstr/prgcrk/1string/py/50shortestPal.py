def main(s):
    for rp in range(1,len(s)+1):
        wrd=s[1:rp][::-1]+s
        if wrd==wrd[::-1]:  return wrd
    
if __name__ == '__main__':
    print(main("aacecaaa"))
    print(main("abcd"))