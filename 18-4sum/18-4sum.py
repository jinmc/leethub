class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for a in range(len(nums)-3):
            for b in range(a+1, len(nums)-2):
                
                l, r = b+1, len(nums)-1
                while l < r:
                    this_sum = nums[a] + nums[b] + nums[l] + nums[r]
                    if this_sum == target:
                        result.add((nums[a], nums[b], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif this_sum < target:
                        l += 1
                    else:
                        r -= 1
                    
        return list(result)