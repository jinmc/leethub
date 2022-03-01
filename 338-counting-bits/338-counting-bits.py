class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            ans = str(bin(i))[2:].count("1")
            print(str(bin(i))[2:].count("1"))
            # ans = bin(str(i))[2:].count("1")
            res.append(ans)
            
        return res
        