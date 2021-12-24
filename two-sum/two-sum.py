class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        this_set = set()
        for num in nums:
            this_set.add(target-num)
        print(this_set)
        for i in range(len(nums)):
            num = nums[i]
            if num in this_set:
                idx = nums.index(target - num)
                if i != idx:
                    return [i, idx]
                
            
