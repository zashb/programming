class Solution:
    def editDistance(self,w1,w2):
        distance = [[i] for i in range(len(w1) + 1)]
        distance[0] = [j for j in range(len(w2) + 1)]

        for i in range(1, len(w1) + 1):
            for j in range(1, len(w2) + 1):
                insert = distance[i][j - 1] + 1
                delete = distance[i - 1][j] + 1
                replace = distance[i - 1][j - 1]
                if w1[i - 1] != w2[j - 1]:
                    replace += 1
                distance[i].append(min(insert, delete, replace))

        return distance[-1][-1]

print(Solution().editDistance("Rabbit", "Racket"))
print(Solution().editDistance("Rabbit", "Rabket"))