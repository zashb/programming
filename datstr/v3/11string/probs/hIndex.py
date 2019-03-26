class Solution:
    def hIndex(self, citations):
        # citations = sorted(citations)
        # for i, j in enumerate(citations):
        #     if j == len(citations[i:]) and len(citations) - (i + 1) == len(citations[:i]):
        #         return j
        #     else:
        #         return None
        #

        citations = sorted(citations)
        # print(citations)
        for i, j in enumerate(citations):
            if j == len(citations[i:]) and len(citations[:i]) < j:
                return j


if __name__ == "__main__":
    print(Solution().hIndex([3, 0, 6, 1, 5]))

# TTR:
# sort the citations
