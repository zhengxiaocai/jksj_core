from ch13.utils.utils import get_sum
from ch13.utils.class_utils import Encoder, Decoder

if __name__ == '__main__':
    print(get_sum(1, 2))

    encoder = Encoder()
    decoder = Decoder()

    print(encoder.encoder('abcde'))
    print(decoder.decoder('edcba'))
