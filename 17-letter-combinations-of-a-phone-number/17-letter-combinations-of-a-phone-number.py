class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        my_dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno",
                  "7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits) < 1:
            return []
        # print(my_dict)
        result = [""]
        for i in digits:
            this_q = list(result)
            result = []
            for this_str in this_q:
                for j in my_dict[i]:
                    # print(j)                    
                    result.append(this_str + j)
        return result
        # print(result)