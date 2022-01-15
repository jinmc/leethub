class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = len(digits) - 1
        carry = 1
        while carry == 1:
            if idx == -1:
                digits.insert(0, 1)
                break
            if digits[idx] == 9:
                digits[idx] = 0
                carry = 1
            else:
                digits[idx] += 1
                carry = 0
            idx -= 1
        return digits