class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # print("-"+s.strip()+"-")
        return len(s.strip().split()[-1])