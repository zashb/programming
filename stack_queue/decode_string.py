"""
comp: O(n)
"""


class Solution:
    def decodeString(self, s):
        stack = [["", 1]]
        num = 0
        for ch in s:
            if ch.isdigit():
              num = num * 10 + ord(ch) - ord("0")
            elif ch == '[':
                stack.append(["", num])
                num = 0
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += ch
        return stack[0][0]


expected = "aaabcbc"
actual = Solution().decodeString("3[a]2[bc]")
print(expected == actual)

expected = "accaccacc"
actual = Solution().decodeString("3[a2[c]]")
print(expected == actual)

expected = "abcabccdcdcdef"
actual = Solution().decodeString("2[abc]3[cd]ef")
print(expected == actual)
