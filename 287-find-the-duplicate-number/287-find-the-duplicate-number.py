class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = 0
        n = len(nums) - 1
        bits = n.bit_length()
        
        for b in range(bits):
            mask = 1 << b
            base_count = 0
            nums_count = 0
            for i in range(n+1):
                if i & mask:
                    base_count += 1
                if nums[i] & mask:
                    nums_count += 1
                    
            if nums_count - base_count > 0:
                dup |= mask
            
        return dup