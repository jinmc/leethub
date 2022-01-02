class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #   1
        # 100
        
        result = 0
        while x>0 or y>0:
            # print(x,y, result)
            if x==0:
                if y%2 ==1:
                    result+=1
                y = y//2
                continue
            if y==0:
                if x%2 ==1:
                    result+=1
                x = x//2
                continue
            if y%2 != x%2:
                result +=1
            y= y//2
            x= x//2
        return result