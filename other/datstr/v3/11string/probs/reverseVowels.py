class Solution:
    def reverseVowels(self, s):
        vowels = [i for i in s if i in 'aeiou']
        res = []
        for char in s:
            if char not in 'aeiou':
                res.append(char)
            else:
                res.append(vowels.pop())

        return "".join(res)


if __name__ == "__main__":
    print(Solution().reverseVowels("hello"))
    print(Solution().reverseVowels("leetcode"))
