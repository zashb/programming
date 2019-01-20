def bullsCows(secret,guess):
    bc,cc,l = 0,0,[0]*10
    for i in range(len(secret)):
        secret_i,guess_i = int(secret[i]),int(guess[i])
        if secret_i == guess_i:  bc += 1
        else:
            if l[secret_i]<0: cc+=1
            if l[guess_i]>0: cc+=1
            l[secret_i]+=1
            l[guess_i]-=1
    return str(bc)+"A"+str(cc)+"B"

if __name__=="__main__":
    print(bullsCows("1807","7810"))
    print(bullsCows("1234","7210"))

# notes
# init l: a list to inc/dec val at int(i)
# bc +=1 straight away
# cc +=1 if <0 or >0