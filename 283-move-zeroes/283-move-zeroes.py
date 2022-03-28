class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pointer = 0
        for i in nums:
            if i != 0:
                nums[non_zero_pointer] = i
                non_zero_pointer += 1
        
        for i in range(non_zero_pointer, len(nums)):
            nums[i] = 0
        
        
