class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def make_dec(num):
            target = 0
            for i in range(len(num)):
                target *= 2
                target += int(num[i])
            return target
            
        num_a, num_b = make_dec(a), make_dec(b)
        # print(num_a, num_b)
        bin_num =  bin(num_a + num_b)
        # print(str(bin_num)[2:])
        return str(bin_num)[2:]