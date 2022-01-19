class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result, current = 0, 0
        for i in range(len(s)):
            this_set = set()
            current = 0
            for j in range(i, len(s)):
                if s[j] in this_set:
                    break
                else:
                    this_set.add(s[j])
                    current += 1
                    # print("current", current)
                    result = max(result, current)
        return result