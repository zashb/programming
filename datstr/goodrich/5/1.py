class CaesarCipher:
    # create forward and backward shifts
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            # ord conv char to ord, chr conv ord to char
            encoder[i] = chr(ord("A") + (i + shift) % 26)
            decoder[i] = chr(ord("A") + (i - shift) % 26)
        # each alpha shifted forward by shift
        self._forward = "".join(encoder)
        # each alpha shifted backwards by shift
        self._backward = "".join(decoder)

    # map each char in msg to forward
    def encrypt(self, msg):
        return self._transform(msg, self._forward)

    # map each char in forward to msg
    def decrypt(self, msg):
        return self._transform(msg, self._backward)

    # map bwn msg to encrypt and decrypt to msg
    def _transform(self, msg, code):
        msgList = list(msg)
        for i, j in enumerate(msgList):
            if j.isupper():
                # j = will not modify in the list
                msgList[i] = code[ord(j) - ord("A")]
        return "".join(msgList)


if __name__ == "__main__":
    a = CaesarCipher(3)
    b = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    c = a.encrypt(b)
    print("code : {}".format(c))
    d = a.decrypt(c)
    print("orig : {}".format(d))
