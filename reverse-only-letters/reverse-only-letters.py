class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        alpha_stack = []
        nonalpha_dict = {}
        result = []
        for i in range(len(s)):
            if s[i].isalpha():
                alpha_stack.append(s[i])
            else:
                nonalpha_dict[i] = s[i]
        for j in range(len(s)):
            if s[j].isalpha():
                result.append(alpha_stack.pop())
            else:
                result.append(nonalpha_dict[j])
                
        
        return "".join(result)
