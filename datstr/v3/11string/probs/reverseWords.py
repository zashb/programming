class Solution:
    def reverseWords(self, s):
        words = s.split(" ")
        revWords = words[::-1]
        return " ".join(revWords)

    # Input: "Let's take LeetCode contest"
    # Output: "s'teL ekat edoCteeL tsetnoc"
    def revChars(self, s):
        words = s.split(" ")
        revChars = [wrd[::-1] for wrd in words]
        return " ".join(revChars)


if __name__ == "__main__":
    print(Solution().reverseWords("the sky is blue"))
    print(Solution().revChars("Let's take LeetCode contest"))
