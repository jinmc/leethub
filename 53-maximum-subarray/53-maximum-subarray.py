class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = global_sum = nums[0]
        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = 0
            current_sum = current_sum + nums[i]            
            global_sum = max(global_sum, current_sum)
            # current_sum = current_sum + nums[i] if current_sum > 0 else nums[i]
            # global_sum = max(global_sum, current_sum)
        return global_sum