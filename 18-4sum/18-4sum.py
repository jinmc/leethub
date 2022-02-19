class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,len(nums)):
                c, d = b + 1, len(nums)-1
                while c < d:
                    this_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if this_sum > target:
                        d -= 1
                    elif this_sum < target:
                        c += 1
                    else:
                        result.add((nums[a], nums[b], nums[c], nums[d]))
                        d -= 1
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
        return list(result)
                # for c in range(b+1,len(nums)):
                #     for d in range(c+1,len(nums)):
                        # if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        #     result.add((nums[a], nums[b], nums[c], nums[d]))
        # return list(result)