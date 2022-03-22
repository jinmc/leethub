class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        c_list = ["a" for _ in range(n)]
        left = k - n
        
        idx = len(c_list) - 1
        while True:
            if left <= 25:
                c_list[idx] = chr(ord('a') + left)
                break
            else:
                c_list[idx] = "z"
                left -= 25
                idx -= 1
        print(c_list)
        return "".join(c_list)
                
                