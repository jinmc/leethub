class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)):
            # print(haystack[i:i+len(needle)], needle)
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
