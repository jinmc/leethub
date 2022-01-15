class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        carry = 1
        while True:
            if idx == -1:
                digits.insert(0, 1)
                break
                
            if digits[idx] + carry < 10:
                digits[idx] = digits[idx] + carry
                break
            else: # 10 이상
                digits[idx] = 0
                carry = 1
                idx -= 1
        return digits