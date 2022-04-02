class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        
        def isPalin(s2):    
            l, r = 0, len(s2)-1
            while l < r:
                if s2[l] != s2[r]:
                    return False
                else:
                    l+=1
                    r-=1
            return True
        
        if isPalin(s):
            return True
        
        while l < r:
            if s[l] != s[r]:
                return isPalin(s[:l]+s[l+1:]) or isPalin(s[:r]+s[r+1:])
            else:
                l+=1
                r-=1