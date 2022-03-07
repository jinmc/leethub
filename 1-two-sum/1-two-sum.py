class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                   answer.append(j)
                   answer.append(i)
        return answer
        
        
        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(len(nums)-1, -1, -1):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]     
        
        
#         for i in range(0, len(nums)): # range(3) -> [0,1,2] i = 0, 1, 2
#             for j in range(len(nums)): # range(i+1, 4) -> range(1,4) [1,2,3], range(2,4) [2,3], range(3,4)
#                 # i = 0, j = 0,1,2,3
#                 # i = 1, j = 0,1,2,3
#                 # i = 2, j = 0,1,2,3
#                 # i = 3, j = 0,1,2,3
#                 if i != j and nums[i] + nums[j] == target:
#                     return [i, j]
            
