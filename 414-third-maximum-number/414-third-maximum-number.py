class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_list = list(set(nums))
        nums_list.sort(reverse=True)
        
        if len(nums_list) < 3:
            return nums_list[0]
        return nums_list[2]