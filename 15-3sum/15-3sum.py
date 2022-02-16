class Solution:
    def threeSum(self, nums):
        # O(n^3) -> O(n^2)
        if len(nums) < 3:
            return []
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            this_set = set()
            
            for j in range(i+1, len(nums)):
                # nums[i], this_num, nums[j]
                # nums[i] + this_num + nums[j] = 0
                # - this_num = nums[i] + nums[j]
                if -(nums[i]+nums[j]) in this_set:
                    result.add((nums[i], -(nums[i] + nums[j]), nums[j]))
                this_set.add(nums[j])
        # print(result)        
        return list(result)