from encoder import GolombEncoder
from decoder import Decoder


class GolombCodec:
    def __init__(self, i: int) -> None:
        self.m = 2**i
        self.encoder = GolombEncoder(i)
        self.decoder = Decoder()

    def encode(self, s: int) -> str:
        return self.encoder.encode(s)

    def decode(self, encoded_number: str) -> int:
        return self.decoder.decode(encoded_number, self.m)


if __name__ == "__main__":
    for i in range(0, 50):
        for s in range(1000):
            golomb_codec = GolombCodec(i)
            encoded_number = golomb_codec.encode(s)
            decoded_number = golomb_codec.decode(encoded_number)
            if s != decoded_number:
                raise Exception(f'expected value {s}, actual value {encoded_number} for i: {i}')
