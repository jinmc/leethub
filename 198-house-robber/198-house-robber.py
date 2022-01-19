class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) == 1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        if len(nums) == 2:
            return dp[1]
        dp[2] = max(nums[0] + nums[2], nums[1])
        if len(nums) == 3:
            return dp[2]
        
        for i in range(3, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[-1]