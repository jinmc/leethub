class Solution:
    def checkString(self, s: str) -> bool:
        b_appears = False
        for i in range(len(s)):
            if b_appears and s[i] == "a":
                return False
            if s[i] == "b":
                b_appears = True
        return True