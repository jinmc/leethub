class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                  "7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits) < 1:
            return []
        # print(my_dict)
        result = [""]
        for digit in digits:
            q = list(result)
            result = []
            for s in q:
                for c in my_dict[digit]:
                    result.append(s + c)
        return result
            