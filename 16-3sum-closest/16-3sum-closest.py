class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r:
                this_sum = nums[i] + nums[l] + nums[r]
                # print("i, l, r: ", i, l, r)
                # print("this_sum", this_sum)
                if abs(this_sum - target) < abs(res - target):
                    res = this_sum
                if this_sum > target:
                    r -= 1
                elif this_sum < target:
                    l += 1
                else:
                    return target
        return res