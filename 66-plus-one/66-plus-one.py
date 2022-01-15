class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        this_num = 0
        for i in range(len(digits)):
            this_num *= 10
            this_num += digits[i]
        print(this_num)
        this_num += 1
        result = list(str(this_num))
        return result
        