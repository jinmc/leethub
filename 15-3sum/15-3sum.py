class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            this_num = nums[i]
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[l] + nums[r] + this_num == 0:
                    res.add((this_num, nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] + this_num > 0:
                    r -= 1
                elif nums[l] + nums[r] + this_num < 0:
                    l += 1
        return list(res)
                