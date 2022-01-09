class Solution:
    # [0,1,3,0,4,0,4,2]
    # [0,1,3,0,4]
    
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        num_len = 0
        for num in nums:
            if num != val:
                temp.append(num)
                num_len += 1
                
        for i in range(num_len):
            nums[i] = temp[i]
        return num_len
        
            