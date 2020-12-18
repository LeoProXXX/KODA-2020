import math 

class GolombEncoder:
    def __init__(self, i: int) -> None:
        self.m = 2**i

    def encode_unary(n: int):
        tmp_arr = []

        for i in range(n):
            tmp_arr.append(1)
            
        tmp_arr.append(0)
        
        tmp_arr_as_string = [str(k) for k in tmp_arr] 
        
        result = "".join(tmp_arr_as_string) 

        return result
    
    def encode_binary(n: int):
        return bin(n)[2:]

    def encode(self, s: int):
        k = int(math.ceil(math.log2(self.m)))
    
        result = GolombEncoder.encode_unary(s//self.m)

        if self.m == 1:
            return result

        return result + GolombEncoder.encode_binary(s % self.m).zfill(k)

if __name__ == "__main__":
    for i in range(0,5):
        print('i:', i)
        for s in range(5):
            print(GolombEncoder(i).encode(s))