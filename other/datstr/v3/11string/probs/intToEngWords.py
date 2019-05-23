class Solution:
    def numberToWords(self, num):
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        # func to build word list
        def _words(n):
            if n < 20:
                onesStr = to19[n - 1:n]
                return onesStr
            if n < 100:
                tensStr = tens[n // 10 - 2]
                onesStr = _words(n % 10)
                # since _words returns a list if n<20, hence just recurse _words(n%10)
                return [tensStr] + onesStr
            if n < 1000:
                hundredsStr = to19[n // 100 - 1]
                tensStr = _words(n % 100)
                return [hundredsStr] + ["Hundred"] + tensStr

        return ' '.join(_words(num)) or 'Zero'


if __name__ == "__main__":
    print(Solution().numberToWords(2))
    print(Solution().numberToWords(21))
    print(Solution().numberToWords(212))
    print(Solution().numberToWords(20))

    # TTR:
    # for to19 do [n-1:n]
