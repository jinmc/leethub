class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                  "7":"pqrs","8":"tuv","9":"wxyz"}
        result = []
        def backtrack(i, s):
            # base case
            if i == len(digits):
                result.append(s)
                return
            # recursion, backtracking
            # else:
            for c in my_dict[digits[i]]:
                backtrack(i+1,s + c)
        
        if digits:
            backtrack(0, "")
        return result
