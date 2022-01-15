class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        this_num = 0
        for i in range(len(digits)):
            this_num *= 10
            this_num += digits[i]
        # print(this_num)
        this_num += 1
        # result = []
        while this_num > 0:
            # result.append(this_num % 10)
            result.insert(0, this_num % 10)
            this_num //= 10
        
        # result = list(str(this_num))
        # result.reverse()
        return result       