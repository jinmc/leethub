class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                  "7":"pqrs","8":"tuv","9":"wxyz"}
        if not digits:
            return []
        result = [""]
        for d in digits:
            q = list(result) # [""] ["a","b","c"] ["ad","ae",...]
            result = []
            for s in q:
                for c in my_dict[d]:
                    result.append(s+c)
        return result
