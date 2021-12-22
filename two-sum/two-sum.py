class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        this_dict={}
        for i in range(len(nums)):
            if nums[i] in this_dict and i!=this_dict[nums[i]]:
                return [i,this_dict[nums[i]]]
            this_dict[target-nums[i]]= i
            
# 7:0
# 2:1          
                
                              
## 바구니에 10000장의 카드
## 3079를 만들어야돼
# [1, 4, 6, 49, 594, 34, 434, ....]
            