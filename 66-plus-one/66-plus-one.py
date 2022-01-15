class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # [9,9,9] => [0,0,0]       
        idx = len(digits) - 1
        carry = 1
        while carry == 1:
            if idx == -1:
                digits.insert(0, 1) # O(N)
                break
            elif digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                carry = 0
            idx -= 1
        return digits