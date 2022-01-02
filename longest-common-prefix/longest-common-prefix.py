class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        substr = strs[0]
        
        def com_pref(s1, s2):
            min_len = min(len(s1), len(s2))
            for i in range(min_len):                
                if s1[i] != s2[i]:
                    return s1[:i]
            return s1[:min_len]
        
        for i in range(1, len(strs)):
            print(substr, strs[i])
            substr = com_pref(substr, strs[i])
        
        return substr
            
            