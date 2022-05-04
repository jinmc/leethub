class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        this_min, this_max = min(nums), max(nums)
        sorted_arr = list(sorted(nums))
        l, r = 0, len(nums)-1
        unchanged = True
        for i in range(len(nums)):
            if sorted_arr[i] != nums[i]:
                l = i
                unchanged = False
                break
        if unchanged:
            return 0
                
        for i in range(len(nums)-1,-1,-1):
            if sorted_arr[i] != nums[i]:
                r = i
                break
        return r - l + 1
        