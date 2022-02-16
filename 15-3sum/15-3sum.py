class Solution:
    def threeSum(self, nums):
        # O(n^3) -> O(n^2)
        if len(nums) < 3:
            return []
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                this_num = nums[i] + nums[l] + nums[r]
                if this_num == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif this_num < 0:
                    l += 1
                elif this_num > 0:
                    r -= 1
        return list(result)
    
# [-4, -1, -1, 0, 1, 2]