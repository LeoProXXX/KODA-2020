import math

class Decoder:

    def countOnes(number: str):
        length = len(number.split("0")[0])
        return length
        
    def getBinaryValueFromSelectedPosition(howManybits: int, code: str):
        if howManybits <= 0:
            return 0
        separatedBitsFromCode = code[-howManybits:] #We have to read them from left side
        return int(separatedBitsFromCode, 2)


    def decode(self, decodedNumber: str, m: int):
        k = int(math.ceil(math.log2(m)))
        t = 2**k - m
        s = Decoder.countOnes(decodedNumber)
        if (k - 1) > 0: # if negative or 0 algorithms might fail
            x = Decoder.getBinaryValueFromSelectedPosition(k, decodedNumber)
            decodedNumber = decodedNumber[:-(k)] #k-1 is wrong
        else:
            x = 0
        if x > t:
            s = s * m + x
        else:
            print(decodedNumber)
            x = x * 2 + int(decodedNumber[-1])
            s = s * m + x - t
        return s


if __name__ == "__main__":
    print(Decoder().decode("10001",8)) #example call






