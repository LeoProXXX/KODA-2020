import math 


class GolombEncoder:
    def __init__(self, i: int) -> None:
        self.m = 2**i

    @staticmethod
    def encode_unary(n: int) -> str:
        tmp_arr = []

        for i in range(n):
            tmp_arr.append(1)
            
        tmp_arr.append(0)
        
        tmp_arr_as_string = [str(k) for k in tmp_arr] 
        
        result = "".join(tmp_arr_as_string) 

        return result

    @staticmethod
    def encode_binary(n: int) -> str:
        return bin(n)[2:]

    def encode(self, s: int) -> str:
        k = int(math.ceil(math.log2(self.m)))
    
        quotient = GolombEncoder.encode_unary(s//self.m)

        if self.m == 1:
            return quotient

        return quotient + GolombEncoder.encode_binary(s % self.m).zfill(k)
    
    def encodeImage(self, array):
        result = []
        for i in array:
            result.append(self.encode(i))
        return result



if __name__ == "__main__":
    for i in range(0,5):
        print('i:', i)
        for s in range(5):
            print(GolombEncoder(i).encode(s))
