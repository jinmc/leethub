class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        ret, cnt = "", 0
        for i in range(n):
            
            # 홀수개
            l, r, this_cnt = i, i, 1
            while l >= 0 and r < n and s[l] == s[r]:
                if this_cnt > cnt:
                    ret = s[l:r+1]
                    cnt = this_cnt
                l -= 1
                r += 1
                this_cnt += 2
            
            # 짝수개
            l, r, this_cnt = i, i+1, 2
            while l >= 0 and r < n and s[l] == s[r]:
                if this_cnt > cnt:
                    ret = s[l:r+1]
                    cnt = this_cnt
                l -= 1
                r += 1
                this_cnt += 2
        return ret