class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e_set = []
        o_set = []
        
        for i in range(len(nums)):
            if nums[i] %2 ==1:
                o_set.append(nums[i])
            else:
                e_set.append(nums[i])
                
        for i in range(len(nums)):
            if i%2 == 0:
                nums[i] = e_set.pop()
            else:
                nums[i] = o_set.pop()
        return nums
                
                