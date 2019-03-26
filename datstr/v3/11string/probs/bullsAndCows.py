import collections


class Solution:
    def bullsAndCows(self, secret, guess):
        # create dicts bwn char and idxs
        secDict = collections.defaultdict(list)
        guesDict = collections.defaultdict(list)
        for idx, char in enumerate(secret):
            secDict[char].append(idx)
        for idx, char in enumerate(guess):
            guesDict[char].append(idx)
        bulCnt, cowCnt = 0, 0
        # for each char in gd, if char in sd, for each idx in sd[char], if idx in gd[char] bc+=1, else cc+=1
        for char in guesDict:
            if char in secDict:
                for idx in secDict[char]:
                    if idx in guesDict[char]:
                        bulCnt += 1
                    else:
                        cowCnt += 1
        return str(bulCnt) + 'A' + str(cowCnt) + 'B'


if __name__ == "__main__":
    print(Solution().bullsAndCows('1807', '7810'))
    print(Solution().bullsAndCows('1123', '0111'))

    # TTR
    # use collections.defaultdict(list) to map char:[index list]
