class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def make_dec(num):
            target = 0
            for i in range(len(num)):
                target *= 2
                target += int(num[i])
            return target
            
        return str(bin(make_dec(a)+ make_dec(b)))[2:]
        