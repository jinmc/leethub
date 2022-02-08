class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalin(s1):
            if s1[::-1] == s1:
                return True
            return False
        # abba
        ret = ""
        n = len(s)
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > len(ret):
                    ret = s[l:r+1]
                l -= 1
                r += 1
                
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if r-l+1 > len(ret): # 새로운 palindrome이 ret보다 길면
                    ret = s[l:r+1]
                l -= 1
                r += 1
        return ret
                    