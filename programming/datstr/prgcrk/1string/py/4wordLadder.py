# return word_ladder length

def wordLadder(start, end, list_words):
    list_words.append(end)
    word_ladder = [(start,1)]
    while word_ladder:
        currword,currlen=word_ladder.pop(0)
        if currword == end: return currlen
        for i in range(len(currword)):
            part1,part2 = currword[:i],currword[i+1:]
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if currword[i]!=j:
                    nextword = part1+j+part2
                    if nextword in list_words:
                        word_ladder.append((nextword, currlen + 1))
                        list_words.remove(nextword)
    return 0


if __name__ == '__main__':
    start = "hit"
    end = "cog"
    list_words = ["hot", "dot", "dog", "lot", "log"]
    print(wordLadder(start, end, list_words))

# algo
# word_ladder = [(word,currlen)]
# pop(0)
# newword = insert alpha at various idx's of currword
# if newword in dict,word_ladder.append((newword,currlen+1)) dict.remove(newword)