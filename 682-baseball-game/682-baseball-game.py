class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        #  ["5","-2","4","C","D","9","+","+"]
        # [5,-2,-4,9,5,14] =>27
        
        result=[]
        
        for i in range(len(ops)):
            if ops[i]=="C":
                result.pop()
            elif ops[i]=="D":
                result.append(result[-1]*2)
            elif ops[i]=="+":
                result.append(result[-1]+result[-2])
            else:
                result.append(int(ops[i]))
                
        return sum(result)
        