class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        this_num = 0
        for i in range(len(digits)):
            this_num *= 10
            this_num += digits[i]
        # print(this_num)
        this_num += 1
        # 124 => [1, 2, 4]
        result = []
        while this_num > 0:
            result.append(this_num % 10)
            this_num //= 10
        # print(result)
        result.reverse()
        return result
        