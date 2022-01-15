class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        after_lastword = False
        result = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and after_lastword:
                break
            elif s[i] != " ":
                result += 1
                after_lastword = True
        return result