class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for a in range(len(nums)-3):
            for b in range(a+1,len(nums)-2):
                # nums[a] + nums[b] + nums[c] + nums[d] == target
                this_dict = {}
                for c in range(b+1, len(nums)):
                    if (target-nums[a]-nums[b]-nums[c]) in this_dict:
                        result.add((nums[a], nums[b], nums[c], target-nums[a]-nums[b]-nums[c]))
                    else:
                        this_dict[nums[c]] = target-nums[a]-nums[b]-nums[c]
        return list(result)