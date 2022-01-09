class Solution:
    # [0,1,3,0,4,0,4,2]
    #          ^
    #                 ^  
    
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c += 1
        return c
        
            