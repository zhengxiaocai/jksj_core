class Encoder:
    def encoder(self, s):
        return s[::-1]


class Decoder:
    def decoder(self, s):
        return ''.join(reversed(list(s)))
