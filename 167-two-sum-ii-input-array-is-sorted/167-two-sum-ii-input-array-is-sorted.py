class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        this_dict = {}
        for i in range(len(numbers)):
            this_dict.update({target-numbers[i] : i})
            
        # print(this_dict)
        result = []
        for i in range(len(numbers)):
            if numbers[i] in this_dict and this_dict[numbers[i]] != i:
                result = [i + 1, this_dict[numbers[i]] + 1]
        
        result.sort()
        return result