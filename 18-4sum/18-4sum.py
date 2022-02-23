class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for a in range(len(nums)-3):
            for b in range(a+1,len(nums)-2):
                # nums[a] + nums[b] + nums[c] + nums[d] == target
                c, d = b+1, len(nums)-1
                while c < d:
                    this_sum = nums[a]+nums[b]+nums[c]+nums[d]
                    if this_sum == target:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                    elif this_sum < target:
                        c += 1
                    else:
                        d -= 1
                        
        return list(result)