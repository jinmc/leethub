class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            this_num = nums[i]
            this_dict = {}
            for j in range(i+1, len(nums)):
                if (-nums[i] - nums[j]) in this_dict:
                    res.add((nums[i], nums[j], - nums[j] - nums[i]))
                this_dict[nums[j]] = - nums[j] - nums[i]
        return list(res)
                