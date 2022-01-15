class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = False
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                result += 1
                flag = True
            elif flag:
                break
        return result                
                
        # return len(s.strip().split()[-1])