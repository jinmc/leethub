class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [a,c,d,e] => max : a
        # [a,c,d,e,b] => max : a + b, b
        # global_max
        this_sum = global_max = nums[0]
        for i in range(1, len(nums)):
            ## 
            if this_sum < 0:
                this_sum = nums[i]
            else:
                this_sum += nums[i]
            ##
            global_max = max(this_sum, global_max)
        return global_max