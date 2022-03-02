class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0, 0
        
        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
            
        if sp == len(s):
            return True
        return False
        