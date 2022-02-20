class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num_list = list(set(nums))
        if len(num_list) < 3:
            return max(num_list)
        first_max = max(num_list) # O(n)
        num_list.pop(num_list.index(first_max)) # O(n)
        second_max = max(num_list)
        num_list.pop(num_list.index(second_max))
        return max(num_list)
            
        
            