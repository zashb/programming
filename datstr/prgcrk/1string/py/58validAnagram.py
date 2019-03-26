def main(s,t):
    alpha=[0]*26
    for i in range(len(s)): alpha[ord(s[i])-ord("a")]+=1
    for i in range(len(t)): alpha[ord(t[i])-ord("a")]-=1
    for i in alpha: 
        if i!=0:    return False    
    return True

if __name__ == '__main__':
    print(main(s = "anagram", t = "nagaram"))
    print(main(s = "rat", t = "car"))