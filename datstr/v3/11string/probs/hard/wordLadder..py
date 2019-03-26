import collections


class Solution(object):
    def ladderLength(self, start, end, wordList):
        # set of words to traverse
        wordSet = set([])
        for word in wordList:
            wordSet.add(word)
        wordLen = len(start)
        queue = collections.deque([(start, 1)])
        while queue:
            currWord, currLen = queue.popleft()
            if currWord == end:
                return currLen
            else:
                for idx in range(wordLen):
                    part1 = currWord[:idx]
                    part2 = currWord[idx + 1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if currWord[idx] != j:
                            nextWord = part1 + j + part2
                            if nextWord in wordSet:
                                queue.append((nextWord, currLen + 1))
                                wordSet.remove(nextWord)
        return 0


if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

    # TTR:
    # deque([(currword,currlen)])
    # non intersecting left and right parts of currword
    # search for the middle part by looping over the alphas
    # if the newword is in wordset append to queue and remove from wordset
