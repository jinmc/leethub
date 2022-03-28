class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # print(k)
        # print(nums[k+1:] + nums[:k+1])
        n = len(nums)
        k %= n
        new_list = [0 for _ in range(n)]
        for i in range(n-k, n):
            new_list[i - (n-k)] = nums[i]
            
        for i in range(n-k):
            new_list[i + (k-n)] = nums[i]
        
        print(new_list)
        for i in range(n):
            nums[i] = new_list[i]
        
        
        # print(nums)
        # rotate_one(nums)
        # print(nums)
            
        # def rotate_one(nums):
#             temp_last = nums[-1]
#             temp, former_temp = nums[1], nums[0]
#             for i in range(1, len(nums)):
#                 # nums[i] = temp
#                 temp = nums[i]
#                 nums[i] = former_temp
#                 former_temp = temp

#             nums[0] = temp_last